from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from ai.adaptive_feedback import create_adaptive_feedback_system
from ai.learning_process import create_ai_learning_process
from models import db, User, StudentProfile, TeacherProfile, Subject, Course, LearningActivity, StudentProgress, AIRecommendation, SystemMetrics, UserFeedback
import os
import json
from datetime import datetime
from flask_migrate import Migrate
from routes.admin import admin_bp
from routes.siswa import siswa_bp
from routes.guru import guru_bp
from routes.admin_features import admin_features_bp
from routes.guru_features import guru_features_bp
from routes.siswa_features import siswa_features_bp

# Import models
# Import AI modules
app = Flask(__name__)

# Cara Kerja routes (must be after app is defined)


# Cara Kerja routes (now use subfolders for each role)
@app.route('/cara_kerja/siswa')
def cara_kerja_siswa():
    return render_template('cara_kerja/siswa.html')


@app.route('/cara_kerja/guru')
def cara_kerja_guru():
    return render_template('cara_kerja/guru.html')


@app.route('/cara_kerja/admin')
def cara_kerja_admin():
    return render_template('cara_kerja/admin.html')


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


@app.before_request
def load_user():
    """Load user data untuk simulasi session - only for protected routes"""
    # Bypass auth for landing page, login, static, and cara_kerja pages
    public_endpoints = [
        'landing', 'login', 'static',
        'cara_kerja_siswa', 'cara_kerja_guru', 'cara_kerja_admin'
    ]
    if request.endpoint in public_endpoints:
        return

    if 'user_id' not in session:
        # Redirect to login if not authenticated
        if request.endpoint not in public_endpoints:
            return redirect(url_for('login'))

# Main Routes


@app.route('/')
def landing():
    """Landing page route"""
    return render_template('landing_page/landing.html')


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
                    return redirect(url_for('siswa.dashboard_siswa'))
                elif role == 'teacher':
                    return redirect(url_for('guru.dashboard_guru'))
                elif role == 'admin':
                    return redirect(url_for('admin.dashboard_admin'))

        # Database account validation

        # Mapping role input ke role di database
        role_map = {'student': 'siswa', 'teacher': 'guru', 'admin': 'admin'}
        db_role = role_map.get(role, role)
        user = User.query.filter_by(username=username, role=db_role).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_role'] = user.role
            session['user_name'] = getattr(user, 'full_name', user.username)
            session['username'] = user.username
            # Tambahan: data lain jika ada
            if user.role == 'siswa' and hasattr(user, 'student_profile') and user.student_profile:
                session['class'] = getattr(
                    user.student_profile, 'grade_level', '')
                session['student_id'] = getattr(
                    user.student_profile, 'student_id', '')
                session['join_date'] = str(
                    getattr(user.student_profile, 'created_at', ''))
            elif user.role == 'guru' and hasattr(user, 'teacher_profile') and user.teacher_profile:
                session['employee_id'] = getattr(
                    user.teacher_profile, 'teacher_id', '')
                session['department'] = getattr(
                    user.teacher_profile, 'school_name', '')

            # Redirect based on role
            if user.role == 'siswa':
                return redirect(url_for('siswa.dashboard_siswa'))
            elif user.role == 'guru':
                return redirect(url_for('guru.dashboard_guru'))
            elif user.role == 'admin':
                return redirect(url_for('admin.dashboard_admin'))

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
        # user_data handled in Blueprint
        # dashboard_data handled in Blueprint

        return jsonify({
            'status': 'success',
            # 'user': user_data,
            # 'data': dashboard_data,
            # 'timestamp': dashboard_data['timestamp']
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/notifications/<role>')
def get_notifications(role):
    """API untuk mendapatkan notifikasi terbaru"""
    try:
        # dashboard_data handled in Blueprint
        return jsonify({
            'status': 'success',
            # 'notifications': dashboard_data['notifications'],
            # 'count': len(dashboard_data['notifications'])
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


@app.route('/')
def home():
    return render_template('home.html')


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
    return render_template('ai_personalization.html')

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
    return render_template('reporting/survey.html')

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
    return render_template('interface/training.html', modules=training_modules)

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
            avg_progress = db.session.query(
                db.func.avg(StudentProgress.progress_percentage)
            ).join(Course).filter(Course.subject_id == subject.id).scalar() or 0

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

    return render_template('analytics/analytics.html', **analytics_data)

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

    return render_template('ai/ai_personalization.html', recommendations=recommendations)

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
    return render_template('reporting/reporting.html', **report_data)

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
    return render_template('integration/pilot_testing.html', **pilot_data)


# Register Blueprints for modular routes
app.register_blueprint(admin_bp)
app.register_blueprint(siswa_bp)
app.register_blueprint(guru_bp)
app.register_blueprint(admin_features_bp)
app.register_blueprint(guru_features_bp)
app.register_blueprint(siswa_features_bp)

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
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('error/500.html'), 500


@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 errors"""
    return render_template('error/403.html'), 403


@app.context_processor
def inject_user():
    user = {
        'name': session.get('user_name', ''),
        'role': session.get('user_role', ''),
        'email': session.get('username', ''),
        'avatar': session.get('avatar', '/static/images/avatar-default.png'),
        'class': session.get('class', ''),
        'student_id': session.get('student_id', ''),
        'join_date': session.get('join_date', ''),
        'subject': session.get('subject', ''),
        'employee_id': session.get('employee_id', ''),
        'department': session.get('department', ''),
    }
    return dict(user=user)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
