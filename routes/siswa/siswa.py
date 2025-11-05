from flask import Blueprint, render_template, session, redirect, url_for, jsonify, request
from ai.learning_process import create_ai_learning_process
from models import db, StudentProfile, LearningActivity, StudentProgress, Course
from datetime import datetime, timedelta
from functools import wraps

siswa_bp = Blueprint('siswa', __name__, url_prefix='/siswa')
ai_learning_process = create_ai_learning_process()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def get_student_data():
    """Helper function to get common student data"""
    user_id = session.get('user_id')
    student = StudentProfile.query.filter_by(user_id=user_id).first()

    if not student and session.get('username') == 'demo_student':
        from models import User
        user = User.query.filter_by(id=user_id).first()
        if user:
            student = StudentProfile(
                user_id=user.id,
                student_id=f'DEMO{user.id}',
                kelas='XII',
                school_name='SMA Demo',
                learning_style='visual',
                learning_pace='normal',
                preferred_subjects='["Matematika", "Fisika"]',
                mslq_level='medium',
                ams_type='intrinsic',
                engagement_level='medium'
            )
            db.session.add(student)
            db.session.commit()
            student = StudentProfile.query.filter_by(user_id=user_id).first()

    return student

# Endpoint untuk update progress dan update Q-learning RL otomatis


@siswa_bp.route('/submit_progress', methods=['POST'])
@login_required
def submit_progress():
    """Update progress siswa dan update Q-learning RL jika selesai (progress 100%)"""
    try:
        user_id = session.get('user_id')
        data = request.get_json()
        course_id = data.get('course_id')
        progress = float(data.get('progress_percentage', 0))

        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        # Update atau buat progress
        sp = StudentProgress.query.filter_by(
            student_id=student.id, course_id=course_id).first()
        if not sp:
            sp = StudentProgress(
                student_id=student.id,
                course_id=course_id,
                progress_percentage=progress
            )
            db.session.add(sp)
        else:
            sp.progress_percentage = progress

        # Record activity
        activity = LearningActivity(
            user_id=user_id,
            activity_type='progress_update',
            details=f'Updated progress for course {course_id} to {progress}%'
        )
        db.session.add(activity)

        db.session.commit()

        # Update Q-learning if course completed
        if progress == 100:
            ql = ai_learning_process.get_qlearning_recommender(student)
            state = ql.get_state(student)
            action = str(course_id)
            reward = 1
            next_state = state
            ql.update(state, action, reward, next_state)

        return jsonify({
            'status': 'success',
            'progress': progress,
            'message': 'Progress updated successfully'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


siswa_bp = Blueprint('siswa', __name__, url_prefix='/siswa')
ai_learning_process = create_ai_learning_process()


@siswa_bp.route('/dashboard')
@login_required
def dashboard_siswa():
    student = get_student_data()
    if not student:
        return redirect(url_for('auth.login'))

    # Basic user data
    user = {
        'name': session.get('user_name', student.student_id),
        'role': 'Siswa',
        'email': session.get('username', 'siswa@lenteramu.id'),
        # 'avatar': '/static/images/avatar-student.png',
        'class': student.kelas,
        'student_id': student.student_id,
        'join_date': student.created_at.strftime('%Y-%m-%d') if student.created_at else '-',
    }

    # Progress Statistics
    progress_records = StudentProgress.query.filter_by(
        student_id=student.id).all()
    total_courses = len(progress_records)
    completed_courses = len(
        [p for p in progress_records if p.progress_percentage == 100])
    pending_tasks = len(
        [p for p in progress_records if 0 < p.progress_percentage < 100])

    # Calculate overall progress
    progress = int(
        (sum([p.progress_percentage for p in progress_records]) / (total_courses or 1)))

    # Recent Activities
    recent_activities = LearningActivity.query.filter_by(
        user_id=student.user_id
    ).order_by(LearningActivity.created_at.desc()).limit(5).all()

    # Calculate Learning Streak
    today = datetime.now().date()
    learning_streak = 0
    last_activity_date = None

    # Get last 30 days of activities to check streak
    activities = LearningActivity.query.filter(
        LearningActivity.user_id == student.user_id,
        LearningActivity.created_at >= today - timedelta(days=30)
    ).order_by(LearningActivity.created_at.desc()).all()

    if activities:
        # Group activities by date
        activity_dates = set(activity.created_at.date()
                             for activity in activities)

        # Start counting from the most recent day
        check_date = today
        while check_date in activity_dates:
            learning_streak += 1
            check_date -= timedelta(days=1)

    # Get AI Recommendations
    recommendations = ai_learning_process.generate_recommendations(student.id)

    # Upcoming Tasks
    upcoming_tasks = Course.query.join(StudentProgress).filter(
        StudentProgress.student_id == student.id,
        StudentProgress.progress_percentage < 100
    ).limit(5).all()

    # Calculate average grade (sample calculation)
    grades = StudentProgress.query.filter_by(student_id=student.id).all()
    average_grade = 85  # Default value
    if grades:
        # Convert grades to integers and handle possible string values
        try:
            total = sum([int(g.grade) if hasattr(g, 'grade') and g.grade is not None
                        else 85 for g in grades])
            average_grade = int(total / len(grades))
        except (ValueError, TypeError):
            # If conversion fails, use default value
            average_grade = 85

    # Calculate total study hours (sample calculation)
    total_study_hours = sum([
        activity.duration_minutes if hasattr(
            activity, 'duration_minutes') and activity.duration_minutes is not None else 30
        for activity in activities
    ]) / 60  # Convert to hours

    if not total_study_hours:
        total_study_hours = 12  # Default value if no data

    context = {
        'user': user,
        'progress': progress,
        'completed_courses': completed_courses,
        'pending_tasks': pending_tasks,
        'total_courses': total_courses,
        'recent_activities': recent_activities,
        'recommendations': recommendations,
        'upcoming_tasks': upcoming_tasks,
        'learning_streak': learning_streak,
        'average_grade': average_grade,
        'total_study_hours': int(total_study_hours),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    return render_template('siswa/dashboard_siswa.html', **context)


@siswa_bp.route('/profile')
@login_required
def profile():
    student = get_student_data()
    if not student:
        return redirect(url_for('auth.login'))

    user = {
        'name': session.get('user_name', student.student_id),
        'role': 'Siswa',
        'email': session.get('username', 'siswa@lenteramu.id'),
        # 'avatar': '/static/images/avatar-student.png',
        'class': student.kelas,
        'student_id': student.student_id,
        'school': student.school_name,
        'join_date': student.created_at.strftime('%Y-%m-%d') if student.created_at else '-',
    }

    return render_template('siswa/profile.html', user=user, student=student)


@siswa_bp.route('/settings')
@login_required
def settings():
    student = get_student_data()
    if not student:
        return redirect(url_for('auth.login'))

    user = {
        'name': session.get('user_name', student.student_id),
        'role': 'Siswa',
        'email': session.get('username', 'siswa@lenteramu.id'),
        # 'avatar': '/static/images/avatar-student.png'
    }

    return render_template('siswa/settings.html', user=user)


@siswa_bp.route('/notifications')
@login_required
def notifications():
    student = get_student_data()
    if not student:
        return redirect(url_for('auth.login'))

    # Example notifications (replace with actual notifications from database)
    notifications = [
        {
            'type': 'assignment',
            'title': 'Tugas Baru',
            'message': 'Tugas Matematika telah ditambahkan',
            'timestamp': datetime.now() - timedelta(hours=2)
        },
        {
            'type': 'achievement',
            'title': 'Pencapaian Baru',
            'message': 'Selamat! Anda telah menyelesaikan 5 materi berturut-turut',
            'timestamp': datetime.now() - timedelta(days=1)
        }
    ]

    user = {
        'name': session.get('user_name', student.student_id),
        'role': 'Siswa',
        # 'avatar': '/static/images/avatar-student.png'
    }

    return render_template('siswa/notifications.html',
                           notifications=notifications,
                           user=user)

# API Routes


@siswa_bp.route('/api/progress_summary')
@login_required
def get_progress_summary():
    student = get_student_data()
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    progress_records = StudentProgress.query.filter_by(
        student_id=student.id).all()

    return jsonify({
        'total_courses': len(progress_records),
        'completed': len([p for p in progress_records if p.progress_percentage == 100]),
        'in_progress': len([p for p in progress_records if 0 < p.progress_percentage < 100]),
        'not_started': len([p for p in progress_records if p.progress_percentage == 0])
    })


@siswa_bp.route('/api/recent_activities')
@login_required
def get_recent_activities():
    student = get_student_data()
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    activities = LearningActivity.query.filter_by(
        user_id=student.user_id
    ).order_by(LearningActivity.created_at.desc()).limit(10).all()

    return jsonify([{
        'type': activity.activity_type,
        'details': activity.details,
        'timestamp': activity.created_at.isoformat()
    } for activity in activities])
