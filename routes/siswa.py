from flask import Blueprint, render_template, session, redirect, url_for, jsonify, request
from ai.learning_process import create_ai_learning_process
from models import db, StudentProfile, LearningActivity, StudentProgress

siswa_bp = Blueprint('siswa', __name__, url_prefix='/siswa')
ai_learning_process = create_ai_learning_process()

# Endpoint untuk update progress dan update Q-learning RL otomatis


@siswa_bp.route('/submit_progress', methods=['POST'])
def submit_progress():
    """Update progress siswa dan update Q-learning RL jika selesai (progress 100%)"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Not logged in'}), 401
    data = request.get_json()
    course_id = data.get('course_id')
    progress = float(data.get('progress_percentage', 0))
    # Cari student profile
    student = StudentProfile.query.filter_by(user_id=user_id).first()
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    # Update atau buat progress
    sp = StudentProgress.query.filter_by(
        student_id=student.id, course_id=course_id).first()
    if not sp:
        sp = StudentProgress(student_id=student.id,
                             course_id=course_id, progress_percentage=progress)
        db.session.add(sp)
    else:
        sp.progress_percentage = progress
    db.session.commit()
    # Jika progress selesai, update Q-learning RL
    if progress == 100:
        from ai.learning_process import create_ai_learning_process
        ai_learning = create_ai_learning_process()
        ql = ai_learning.get_qlearning_recommender(student)
        state = ql.get_state(student)
        action = str(course_id)
        reward = 1
        next_state = state
        ql.update(state, action, reward, next_state)
    return jsonify({'status': 'success', 'progress': progress})


siswa_bp = Blueprint('siswa', __name__, url_prefix='/siswa')
ai_learning_process = create_ai_learning_process()


@siswa_bp.route('/dashboard')
def dashboard_siswa():
    user_id = session.get('user_id')
    student = StudentProfile.query.filter_by(user_id=user_id).first()
    # Jika user demo siswa login dan belum ada profil, auto-create profil demo
    if not student and session.get('username') == 'demo_student':
        from models import User
        user = User.query.filter_by(id=user_id).first()
        if user:
            import random
            student = StudentProfile(
                user_id=user.id,
                student_id=f'DEMO{user.id}',
                grade_level='XII',
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
    # Cek ulang setelah auto-create
    student = StudentProfile.query.filter_by(user_id=user_id).first()
    if not student:
        return render_template('landing_page/landing.html', error='Profil siswa tidak ditemukan. Silakan hubungi admin.')
    # Data user
    user = {
        'name': session.get('user_name', student.student_id),
        'role': session.get('user_role', 'student'),
        'email': session.get('username', 'siswa@lenteramu.id'),
        'avatar': '/static/images/avatar-student.png',
        'class': student.grade_level,
        'student_id': student.student_id,
        'join_date': student.created_at.strftime('%Y-%m-%d') if student.created_at else '-',
    }
    # Progress statistik
    progress_records = StudentProgress.query.filter_by(
        student_id=student.id).all()
    total_courses = len(progress_records)
    completed_courses = len(
        [p for p in progress_records if p.progress_percentage == 100])
    pending_tasks = len(
        [p for p in progress_records if 0 < p.progress_percentage < 100])
    progress = int(
        (sum([p.progress_percentage for p in progress_records]) / (total_courses or 1)))
    average_grade = '-'
    grades = [float(p.grade) for p in progress_records if p.grade and p.grade.replace(
        '.', '', 1).isdigit()]
    if grades:
        average_grade = round(sum(grades)/len(grades), 2)
    learning_streak = 0  # Placeholder, bisa dihitung dari log aktivitas
    total_study_hours = 0  # Placeholder, bisa dihitung dari LearningActivity
    # Subjects
    subjects = []
    for p in progress_records:
        subj = {
            'name': p.course.subject.name if hasattr(p, 'course') and hasattr(p.course, 'subject') else '-',
            'grade': p.grade or '-',
            'progress': int(p.progress_percentage)
        }
        subjects.append(subj)
    # Notifikasi (dummy, bisa diambil dari tabel notifikasi jika ada)
    notifications = [
        {'type': 'assignment', 'message': 'Tugas baru tersedia!', 'time': 'Hari ini'},
        {'type': 'grade', 'message': 'Nilai kuis telah keluar.', 'time': 'Kemarin'},
        {'type': 'announcement', 'message': 'Jadwal ujian telah diumumkan.',
            'time': '2 hari lalu'},
    ]
    # Upcoming exams (dummy, bisa diambil dari tabel ujian jika ada)
    upcoming_exams = [
        {'date': '2025-09-20', 'subject': 'Matematika', 'type': 'UTS'},
        {'date': '2025-09-25', 'subject': 'Fisika', 'type': 'Kuis'},
    ]
    context = {
        'user': user,
        'student_name': user['name'],
        'user_role': 'student',
        'progress': progress,
        'completed_courses': completed_courses,
        'pending_tasks': pending_tasks,
        'average_grade': average_grade,
        'learning_streak': learning_streak,
        'total_study_hours': total_study_hours,
        'subjects': subjects,
        'notifications': notifications,
        'upcoming_exams': upcoming_exams,
        'timestamp': student.created_at.strftime('%Y-%m-%d') if student.created_at else '-',
    }
    return render_template('siswa/dashboard_siswa.html', **context)


@siswa_bp.route('/workflow')
def student_workflow():
    try:
        user_id = session.get('user_id')
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if not student:
            return redirect(url_for('home'))
        recent_activities = LearningActivity.query.filter_by(user_id=user_id).order_by(
            LearningActivity.created_at.desc()).limit(5).all()
        progress_records = StudentProgress.query.filter_by(
            student_id=student.id).all()
        recommendations = ai_learning_process.generate_recommendations(
            student.id)
        user = {
            'name': session.get('user_name', 'Demo Student'),
            'role': session.get('user_role', 'student'),
            'email': session.get('username', 'siswa@lenteramu.id'),
        }
        workflow_data = {
            'student': student,
            'recent_activities': [a.to_dict() for a in recent_activities],
            'progress_summary': {
                'total_courses': len(progress_records),
                'completed': len([p for p in progress_records if p.progress_percentage == 100]),
                'in_progress': len([p for p in progress_records if 0 < p.progress_percentage < 100]),
                'not_started': len([p for p in progress_records if p.progress_percentage == 0])
            },
            'ai_recommendations': recommendations,
            'user': user
        }
        return render_template('workflows/student_workflow.html', **workflow_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
