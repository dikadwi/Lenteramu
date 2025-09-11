from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import json
import os

# Import models
from models import db, User, StudentProfile, TeacherProfile, Subject, Course, LearningActivity, StudentProgress, AIRecommendation, SystemMetrics, UserFeedback

# Import AI modules
from ai.learning_process import create_ai_learning_process
from ai.adaptive_feedback import create_adaptive_feedback_system

app = Flask(__name__)

# Database Configuration
app.config['SECRET_KEY'] = 'lenteramu-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL') or 'mysql+pymysql://root:@localhost:3306/lenteramu_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': 300,
    'pool_pre_ping': True
}

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Initialize AI systems
ai_learning_process = create_ai_learning_process()
adaptive_feedback_system = create_adaptive_feedback_system()

# Session management


def get_user_data(user_id=None, role=None):
    """Get user data based on session or parameters"""
    if not user_id:
        user_id = session.get('user_id')
    if not role:
        role = session.get('user_role')

    # Mock data untuk demo yang lebih dinamis
    mock_users = {
        'student': {
            'id': 1,
            'name': 'Ahmad Rizki Pratama',
            'email': 'ahmad.rizki@student.lenteramu.id',
            'avatar': '/static/images/avatar-student.png',
            'class': 'XII IPA 1',
            'student_id': 'STD2024001',
            'join_date': '2024-01-15'
        },
        'teacher': {
            'id': 2,
            'name': 'Dr. Siti Nurhaliza',
            'email': 'siti.nurhaliza@teacher.lenteramu.id',
            'avatar': '/static/images/avatar-teacher.png',
            'subject': 'Matematika',
            'employee_id': 'TCH2024001',
            'join_date': '2020-08-01'
        },
        'admin': {
            'id': 3,
            'name': 'Budi Santoso',
            'email': 'budi.santoso@admin.lenteramu.id',
            'avatar': '/static/images/avatar-admin.png',
            'department': 'IT Administration',
            'employee_id': 'ADM2024001',
            'join_date': '2019-03-15'
        }
    }

    return mock_users.get(role, {})


def get_dynamic_dashboard_data(role):
    """Get dynamic dashboard data based on role"""
    import random
    from datetime import datetime, timedelta

    base_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'notifications': [],
        'recent_activities': [],
        'quick_actions': []
    }

    if role == 'student':
        base_data.update({
            'progress': random.randint(70, 95),
            'completed_courses': random.randint(8, 15),
            'pending_tasks': random.randint(2, 8),
            'average_grade': random.choice(['A', 'A-', 'B+', 'B']),
            'learning_streak': random.randint(5, 30),
            'total_study_hours': random.randint(45, 120),
            'subjects': [
                {'name': 'Matematika', 'progress': random.randint(
                    70, 100), 'grade': 'A'},
                {'name': 'Fisika', 'progress': random.randint(
                    60, 95), 'grade': 'B+'},
                {'name': 'Kimia', 'progress': random.randint(
                    65, 90), 'grade': 'A-'},
                {'name': 'Biologi', 'progress': random.randint(
                    75, 100), 'grade': 'A'},
                {'name': 'Bahasa Indonesia',
                    'progress': random.randint(80, 100), 'grade': 'A'},
            ],
            'upcoming_exams': [
                {'subject': 'Matematika', 'date': '2025-09-10',
                    'type': 'Ujian Tengah Semester'},
                {'subject': 'Fisika', 'date': '2025-09-12', 'type': 'Quiz Mingguan'},
                {'subject': 'Kimia', 'date': '2025-09-15', 'type': 'Praktikum'},
            ],
            'notifications': [
                {'type': 'assignment', 'message': 'Tugas Matematika: Integral batas akhir besok',
                    'time': '2 jam lalu'},
                {'type': 'grade', 'message': 'Nilai Quiz Fisika telah keluar: A-',
                    'time': '5 jam lalu'},
                {'type': 'announcement', 'message': 'Pengumuman: Libur nasional 17 Agustus',
                    'time': '1 hari lalu'},
            ]
        })

    elif role == 'teacher':
        base_data.update({
            'total_students': random.randint(120, 180),
            'total_classes': random.randint(8, 12),
            'pending_grading': random.randint(15, 45),
            'average_class_performance': random.randint(75, 90),
            'classes': [
                {'name': 'XII IPA 1', 'students': 32,
                    'avg_score': random.randint(80, 95)},
                {'name': 'XII IPA 2', 'students': 30,
                    'avg_score': random.randint(75, 90)},
                {'name': 'XI IPA 1', 'students': 35,
                    'avg_score': random.randint(70, 85)},
                {'name': 'XI IPA 2', 'students': 33,
                    'avg_score': random.randint(75, 88)},
            ],
            'recent_assignments': [
                {'class': 'XII IPA 1', 'title': 'Integral Tentu',
                    'submitted': 28, 'total': 32},
                {'class': 'XII IPA 2', 'title': 'Fungsi Trigonometri',
                    'submitted': 25, 'total': 30},
                {'class': 'XI IPA 1', 'title': 'Limit Fungsi',
                    'submitted': 30, 'total': 35},
            ],
            'schedule_today': [
                {'time': '07:00-08:30', 'class': 'XII IPA 1', 'subject': 'Matematika'},
                {'time': '08:30-10:00', 'class': 'XI IPA 2', 'subject': 'Matematika'},
                {'time': '10:30-12:00', 'class': 'XII IPA 2', 'subject': 'Matematika'},
            ],
            'notifications': [
                {'type': 'assignment', 'message': '15 tugas menunggu penilaian dari XII IPA 1',
                    'time': '1 jam lalu'},
                {'type': 'meeting', 'message': 'Rapat koordinasi guru pukul 14:00',
                    'time': '3 jam lalu'},
                {'type': 'system', 'message': 'Sistem penilaian telah diperbarui',
                    'time': '1 hari lalu'},
            ]
        })

    elif role == 'admin':
        base_data.update({
            'total_users': random.randint(800, 1200),
            'total_teachers': random.randint(45, 65),
            'total_students': random.randint(750, 1100),
            'system_uptime': '99.8%',
            'server_status': 'Online',
            'database_size': f"{random.randint(150, 250)} MB",
            'daily_active_users': random.randint(400, 800),
            'user_stats': [
                {'role': 'Students', 'count': random.randint(
                    750, 1100), 'active': random.randint(400, 600)},
                {'role': 'Teachers', 'count': random.randint(
                    45, 65), 'active': random.randint(30, 50)},
                {'role': 'Admins', 'count': random.randint(
                    3, 8), 'active': random.randint(2, 5)},
            ],
            'system_metrics': {
                'cpu_usage': random.randint(20, 60),
                'memory_usage': random.randint(40, 75),
                'disk_usage': random.randint(30, 70),
                'network_traffic': f"{random.randint(50, 200)} MB/h"
            },
            'recent_logs': [
                {'type': 'login', 'message': 'User ahmad.rizki logged in successfully',
                    'time': '5 menit lalu'},
                {'type': 'system', 'message': 'Database backup completed',
                    'time': '1 jam lalu'},
                {'type': 'error', 'message': 'Failed login attempt from 192.168.1.100',
                    'time': '2 jam lalu'},
            ],
            'notifications': [
                {'type': 'system', 'message': 'Server maintenance dijadwalkan Minggu 14:00',
                    'time': '2 jam lalu'},
                {'type': 'alert', 'message': 'Disk usage mencapai 85%',
                    'time': '4 jam lalu'},
                {'type': 'update', 'message': 'Update sistem berhasil diinstall',
                    'time': '1 hari lalu'},
            ]
        })

    return base_data


@app.before_request
def load_user():
    """Load user data untuk simulasi session - only for protected routes"""
    # Bypass auth for landing page and login
    if request.endpoint in ['landing', 'login', 'static']:
        return

    if 'user_id' not in session:
        # Redirect to login if not authenticated
        if request.endpoint not in ['landing', 'login']:
            return redirect(url_for('login'))

# Main Routes


@app.route('/')
def landing():
    """Landing page route"""
    return render_template('landing.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page route"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')

        # Demo account validation
        demo_accounts = {
            'demo_student': {'password': 'demo123', 'role': 'student'},
            'demo_teacher': {'password': 'demo123', 'role': 'teacher'},
            'demo_admin': {'password': 'demo123', 'role': 'admin'}
        }

        if username in demo_accounts:
            demo_user = demo_accounts[username]
            if demo_user['password'] == password and demo_user['role'] == role:
                # Create session
                session['user_id'] = 1  # Demo user ID
                session['user_role'] = role
                session['user_name'] = f"Demo {role.title()}"
                session['username'] = username

                # Redirect based on role
                if role == 'student':
                    return redirect(url_for('dashboard_siswa'))
                elif role == 'teacher':
                    return redirect(url_for('teacher_workflow'))
                elif role == 'admin':
                    return redirect(url_for('dashboard_admin'))

        # If validation fails
        return render_template('login.html', error='Username atau password salah!')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout route"""
    session.clear()
    return redirect(url_for('landing'))

# API Routes untuk fitur dinamis


@app.route('/api/dashboard/refresh/<role>')
def refresh_dashboard_data(role):
    """API untuk refresh data dashboard"""
    try:
        user_data = get_user_data()
        dashboard_data = get_dynamic_dashboard_data(role)

        return jsonify({
            'status': 'success',
            'user': user_data,
            'data': dashboard_data,
            'timestamp': dashboard_data['timestamp']
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/notifications/<role>')
def get_notifications(role):
    """API untuk mendapatkan notifikasi terbaru"""
    try:
        dashboard_data = get_dynamic_dashboard_data(role)
        return jsonify({
            'status': 'success',
            'notifications': dashboard_data['notifications'],
            'count': len(dashboard_data['notifications'])
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/student/progress/<int:student_id>')
def get_student_progress(student_id):
    """API untuk mendapatkan progress siswa"""
    try:
        # Simulasi data progress
        import random
        subjects = ['Matematika', 'Fisika',
                    'Kimia', 'Biologi', 'Bahasa Indonesia']

        progress_data = []
        for subject in subjects:
            progress_data.append({
                'subject': subject,
                'progress': random.randint(60, 100),
                'last_activity': f"{random.randint(1, 7)} hari lalu",
                'grade': random.choice(['A', 'A-', 'B+', 'B', 'B-'])
            })

        return jsonify({
            'status': 'success',
            'student_id': student_id,
            'progress': progress_data,
            'overall_average': sum([p['progress'] for p in progress_data]) / len(progress_data)
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/teacher/classes')
def get_teacher_classes():
    """API untuk mendapatkan data kelas guru"""
    try:
        # Simulasi data kelas
        import random
        classes_data = []

        class_names = ['XII IPA 1', 'XII IPA 2', 'XI IPA 1', 'XI IPA 2']
        for class_name in class_names:
            classes_data.append({
                'name': class_name,
                'students': random.randint(28, 35),
                'avg_score': random.randint(75, 95),
                'last_meeting': f"{random.randint(1, 3)} hari lalu",
                'next_assignment': f"Tugas {random.randint(1, 10)}"
            })

        return jsonify({
            'status': 'success',
            'classes': classes_data,
            'total_students': sum([c['students'] for c in classes_data])
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/admin/system-stats')
def get_system_stats():
    """API untuk mendapatkan statistik sistem real-time"""
    try:
        import random
        from datetime import datetime

        stats = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'cpu_usage': random.randint(20, 80),
            'memory_usage': random.randint(40, 90),
            'disk_usage': random.randint(30, 70),
            'active_users': random.randint(50, 200),
            'network_traffic': f"{random.randint(50, 500)} MB/h",
            'response_time': f"{random.randint(50, 200)} ms"
        }

        return jsonify({
            'status': 'success',
            'stats': stats
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# --- AI Learning Process Routes ---


@app.route('/ai/train-model', methods=['POST'])
def train_ai_model():
    """Endpoint untuk training AI model sesuai alur pembelajaran AI"""
    try:
        # 1. Data Collection
        data = ai_learning_process.data_collection()
        if data.empty:
            return jsonify({'error': 'Insufficient data for training'}), 400

        # 2. Data Preprocessing
        X, y = ai_learning_process.data_preprocessing(data)
        if X is None:
            return jsonify({'error': 'Data preprocessing failed'}), 400

        # 3. Model Training
        training_success = ai_learning_process.model_training(X, y)
        if not training_success:
            return jsonify({'error': 'Model training failed'}), 400

        # 4. Model Validation
        validation_success = ai_learning_process.model_validation(X, y)
        if not validation_success:
            return jsonify({'error': 'Model validation failed'}), 400

        # 5. Model Deployment
        deployment_success = ai_learning_process.model_deployment()
        if not deployment_success:
            return jsonify({'error': 'Model deployment failed'}), 400

        return jsonify({
            'status': 'success',
            'message': 'AI model trained and deployed successfully',
            'metrics': ai_learning_process.performance_metrics,
            'timestamp': datetime.utcnow().isoformat()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/ai/monitor-model', methods=['GET'])
def monitor_ai_model():
    """Endpoint untuk monitoring AI model"""
    try:
        monitoring_result = ai_learning_process.model_monitoring()
        return jsonify(monitoring_result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/ai/generate-recommendations/<int:student_id>')
def generate_ai_recommendations(student_id):
    """Generate AI recommendations untuk siswa"""
    try:
        recommendations = ai_learning_process.generate_recommendations(
            student_id)
        return jsonify({
            'status': 'success',
            'student_id': student_id,
            'recommendations': recommendations
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Adaptive Feedback Routes ---


@app.route('/assessment/submit', methods=['POST'])
def submit_assessment():
    """Submit hasil assessment dan generate adaptive feedback"""
    try:
        data = request.get_json()
        user_id = data.get('user_id') or session.get('user_id')
        course_id = data.get('course_id')
        assessment_result = data.get('result')

        if not all([user_id, course_id, assessment_result]):
            return jsonify({'error': 'Missing required data'}), 400

        # 1. Collect Assessment Data
        collection_result = adaptive_feedback_system.collect_assessment_data(
            user_id, course_id, assessment_result
        )

        if collection_result['status'] != 'success':
            return jsonify(collection_result), 400

        # 2. Analyze Performance
        performance_analysis = adaptive_feedback_system.analyze_student_performance(
            user_id)

        # 3. Generate Adaptive Feedback
        feedback = adaptive_feedback_system.generate_adaptive_feedback(
            performance_analysis)

        # 4. Integrate with UI
        ui_integration = adaptive_feedback_system.integrate_with_ui(
            user_id, feedback)

        # 5. Recommend Additional Content
        content_recommendations = adaptive_feedback_system.recommend_additional_content(
            performance_analysis)

        return jsonify({
            'status': 'success',
            'feedback': feedback,
            'recommendations': content_recommendations,
            'ui_integration': ui_integration,
            'performance_summary': performance_analysis
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/feedback/monitor/<int:user_id>')
def monitor_learning_progress(user_id):
    """Monitor dan adjust pembelajaran siswa"""
    try:
        monitoring_result = adaptive_feedback_system.monitor_and_adjust(
            user_id)
        return jsonify({
            'status': 'success',
            'monitoring': monitoring_result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- User Workflow Routes (Alur Kerja Pengguna) ---


@app.route('/student/workflow')
def student_workflow():
    """Alur kerja siswa sesuai dokumen"""
    try:
        user_id = session.get('user_id')
        student = StudentProfile.query.filter_by(user_id=user_id).first()

        if not student:
            return redirect(url_for('home'))

        # Get student workflow data
        recent_activities = LearningActivity.query.filter_by(user_id=user_id).order_by(
            LearningActivity.created_at.desc()
        ).limit(5).all()

        progress_records = StudentProgress.query.filter_by(
            student_id=student.id).all()
        recommendations = ai_learning_process.generate_recommendations(
            student.id)

        workflow_data = {
            'student': student,
            'recent_activities': [a.to_dict() for a in recent_activities],
            'progress_summary': {
                'total_courses': len(progress_records),
                'completed': len([p for p in progress_records if p.progress_percentage == 100]),
                'in_progress': len([p for p in progress_records if 0 < p.progress_percentage < 100]),
                'not_started': len([p for p in progress_records if p.progress_percentage == 0])
            },
            'ai_recommendations': recommendations
        }

        return render_template('workflows/student_workflow.html', **workflow_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/teacher/workflow')
def teacher_workflow():
    """Dashboard guru dengan data dinamis"""
    # Get user data dan dashboard data
    user_data = get_user_data()
    dashboard_data = get_dynamic_dashboard_data('teacher')

    # Combine data
    context = {
        'user': user_data,
        'teacher_name': user_data.get('name', 'Demo Teacher'),
        'user_role': 'teacher',
        **dashboard_data
    }

    return render_template('workflows/teacher_workflow.html', **context)


@app.route('/admin/workflow')
def admin_workflow():
    """Alur kerja administrator sesuai dokumen"""
    try:
        # System metrics untuk admin
        total_users = User.query.count()
        active_users = User.query.filter_by(is_active=True).count()
        system_metrics = SystemMetrics.query.order_by(
            SystemMetrics.recorded_at.desc()).limit(10).all()

        # Recent activities
        recent_activities = LearningActivity.query.order_by(
            LearningActivity.created_at.desc()
        ).limit(20).all()

        workflow_data = {
            'total_users': total_users,
            'active_users': active_users,
            'system_health': {
                'uptime': '99.8%',
                'response_time': '120ms',
                'error_rate': '0.2%'
            },
            'metrics': [m.to_dict() for m in system_metrics],
            'recent_activities': [a.to_dict() for a in recent_activities]
        }

        return render_template('workflows/admin_workflow.html', **workflow_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def home():
    return render_template('home.html')

# --- Dashboard Siswa ---


@app.route('/dashboard/siswa')
def dashboard_siswa():
    """Dashboard siswa dengan data dinamis"""
    # Get user data dan dashboard data
    user_data = get_user_data()
    dashboard_data = get_dynamic_dashboard_data('student')

    # Combine data
    context = {
        'user': user_data,
        'student_name': user_data.get('name', 'Demo Student'),
        'user_role': 'student',
        **dashboard_data
    }

    return render_template('dashboard_siswa.html', **context)

# --- Dashboard Admin ---


@app.route('/dashboard/admin')
def dashboard_admin():
    """Dashboard admin dengan data dinamis"""
    # Get user data dan dashboard data
    user_data = get_user_data()
    dashboard_data = get_dynamic_dashboard_data('admin')

    # Combine data
    context = {
        'user': user_data,
        'admin_name': user_data.get('name', 'Demo Admin'),
        'user_role': 'admin',
        **dashboard_data
    }

    return render_template('dashboard_admin.html', **context)

# --- Modul Retraining Model AI ---


@app.route('/ai/retrain', methods=['GET', 'POST'])
def retrain_model():
    if request.method == 'POST':
        # Simulasi retraining
        return jsonify({
            'status': 'success',
            'message': 'Model AI berhasil diretrain dengan data terbaru',
            'timestamp': datetime.now().isoformat()
        })
    return render_template('ai_retrain.html')

# --- Monitoring & Evaluasi Implementasi ---


@app.route('/monitoring', methods=['GET'])
def monitoring():
    monitoring_data = {
        'system_status': 'Online',
        'active_users': 234,
        'model_accuracy': 94.2,
        'response_time': '120ms',
        'last_updated': datetime.now().strftime('%H:%M:%S')
    }
    return render_template('monitoring.html', **monitoring_data)

# --- Survei & Umpan Balik Pengguna ---


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        feedback_data = request.get_json()
        # Simpan feedback ke database
        return jsonify({
            'status': 'success',
            'message': 'Terima kasih atas feedback Anda!'
        })
    return render_template('survey.html')

# --- Pelatihan Pengguna & Kompetensi Guru ---


@app.route('/training', methods=['GET'])
def training():
    training_modules = [
        {'title': 'Pengenalan LENTERAMU',
            'duration': '30 menit', 'status': 'completed'},
        {'title': 'Menggunakan AI Personalisasi',
            'duration': '45 menit', 'status': 'in_progress'},
        {'title': 'Analytics & Reporting',
            'duration': '60 menit', 'status': 'pending'},
        {'title': 'Troubleshooting Umum', 'duration': '20 menit', 'status': 'pending'}
    ]
    return render_template('training.html', modules=training_modules)

# --- Analisis Data Siswa ---


@app.route('/analytics/student')
def analytics_student():
    try:
        # Get real analytics data from database
        total_students = User.query.filter_by(role='siswa').count()

        # Calculate engagement rate (students with recent activity)
        recent_activities = LearningActivity.query.filter(
            LearningActivity.created_at >= datetime.utcnow().replace(day=1)
        ).count()
        engagement_rate = (recent_activities / max(total_students, 1)) * 100

        # Calculate completion rate
        completed_progress = StudentProgress.query.filter(
            StudentProgress.progress_percentage == 100
        ).count()
        total_progress = StudentProgress.query.count()
        completion_rate = (completed_progress / max(total_progress, 1)) * 100

        # Calculate satisfaction score from feedback
        avg_rating = db.session.query(db.func.avg(
            UserFeedback.rating)).scalar() or 4.6

        # Get learning trends by subject
        learning_trends = []
        subjects = Subject.query.all()
        for subject in subjects:
            courses_count = Course.query.filter_by(
                subject_id=subject.id).count()
            avg_progress = db.session.query(db.func.avg(StudentProgress.progress_percentage))\
                .join(Course).filter(Course.subject_id == subject.id).scalar() or 0

            learning_trends.append({
                'subject': subject.name,
                'progress': int(avg_progress),
                'students': courses_count * 50  # Estimate
            })

        analytics_data = {
            'total_students': total_students,
            'engagement_rate': round(engagement_rate, 1),
            'completion_rate': round(completion_rate, 1),
            'satisfaction_score': round(avg_rating, 1),
            'learning_trends': learning_trends
        }
    except Exception as e:
        print(f"Database error: {e}")
        # Fallback data
        analytics_data = {
            'total_students': 1250,
            'engagement_rate': 87.5,
            'completion_rate': 92.3,
            'satisfaction_score': 4.6,
            'learning_trends': [
                {'subject': 'Matematika', 'progress': 88, 'students': 450},
                {'subject': 'Sains', 'progress': 92, 'students': 380},
                {'subject': 'Bahasa', 'progress': 85, 'students': 420}
            ]
        }

    return render_template('analytics.html', **analytics_data)

# --- Personalisasi Konten ---


@app.route('/ai/personalization')
def ai_personalization():
    try:
        # Get AI recommendations from database
        # For demo, get recommendations for first student
        student = User.query.filter_by(role='siswa').first()
        if student:
            recommendations_query = AIRecommendation.query.filter_by(
                user_id=student.id,
                is_active=True
            ).join(Course).all()

            recommendations = []
            for rec in recommendations_query:
                recommendations.append({
                    'title': rec.course.title,
                    'type': rec.course.content_type.title(),
                    'match': int(rec.match_score),
                    'duration': f"{rec.course.duration_minutes} menit"
                })
        else:
            recommendations = []

        # Fallback if no recommendations found
        if not recommendations:
            recommendations = [
                {'title': 'Algoritma Sorting', 'type': 'Video',
                    'match': 95, 'duration': '25 menit'},
                {'title': 'Struktur Data Tree', 'type': 'Artikel',
                    'match': 88, 'duration': '15 menit'},
                {'title': 'Kuis Pemrograman Dasar', 'type': 'Quiz',
                    'match': 92, 'duration': '10 menit'},
                {'title': 'Project Web Development', 'type': 'Praktik',
                    'match': 85, 'duration': '2 jam'}
            ]

    except Exception as e:
        print(f"Database error: {e}")
        # Fallback data
        recommendations = [
            {'title': 'Algoritma Sorting', 'type': 'Video',
                'match': 95, 'duration': '25 menit'},
            {'title': 'Struktur Data Tree', 'type': 'Artikel',
                'match': 88, 'duration': '15 menit'},
            {'title': 'Kuis Pemrograman Dasar', 'type': 'Quiz',
                'match': 92, 'duration': '10 menit'},
            {'title': 'Project Web Development', 'type': 'Praktik',
                'match': 85, 'duration': '2 jam'}
        ]

    return render_template('ai_personalization.html', recommendations=recommendations)

# --- Laporan & Visualisasi ---


@app.route('/reporting/report')
def reporting_report():
    report_data = {
        'weekly_progress': [65, 70, 75, 80, 85, 88, 92],
        'subject_performance': {
            'Matematika': 88,
            'Sains': 92,
            'Bahasa Indonesia': 85,
            'Sejarah': 78,
            'Geografi': 82
        },
        'learning_time': {
            'total_hours': 45.5,
            'avg_daily': 6.5,
            'most_active_day': 'Rabu'
        }
    }
    return render_template('reporting.html', **report_data)

# --- Pilot Testing & Evaluasi Bertahap ---


@app.route('/pilot-testing', methods=['GET'])
def pilot_testing():
    pilot_data = {
        'active_pilots': 5,
        'completed_pilots': 12,
        'success_rate': 94.2,
        'pilot_schools': [
            {'name': 'SMA Negeri 1 Jakarta', 'status': 'Aktif', 'progress': 85},
            {'name': 'SMP Labschool', 'status': 'Selesai', 'progress': 100},
            {'name': 'SMK Telkom Bandung', 'status': 'Aktif', 'progress': 72}
        ]
    }
    return render_template('pilot_testing.html', **pilot_data)


# Add database initialization route and main block
@app.route('/init-database')
def init_database_route():
    """Initialize database with sample data"""
    try:
        # Create all tables
        db.create_all()

        # Check if data already exists
        if User.query.first():
            return jsonify({'message': 'Database already initialized'})

        # Import and run initialization
        from init_db import init_database
        init_database()

        return jsonify({'message': 'Database initialized successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error Handlers


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('500.html'), 500


@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 errors"""
    return render_template('403.html'), 403


if __name__ == "__main__":
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
    app.run(debug=True)
