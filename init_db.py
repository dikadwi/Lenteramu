# Database initialization and sample data seeding
from models import *
from app import app
import json


def init_database():
    """Initialize database tables and create sample data"""
    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if data already exists
        if User.query.first():
            print("Database already has data. Skipping initialization.")
            return

        print("Creating sample data...")

        # Create subjects
        subjects = [
            Subject(name='Matematika', code='MTK',
                    description='Mata pelajaran matematika', grade_level='SMA'),
            Subject(name='Fisika', code='FIS',
                    description='Mata pelajaran fisika', grade_level='SMA'),
            Subject(name='Kimia', code='KIM',
                    description='Mata pelajaran kimia', grade_level='SMA'),
            Subject(name='Biologi', code='BIO',
                    description='Mata pelajaran biologi', grade_level='SMA'),
            Subject(name='Bahasa Indonesia', code='BIN',
                    description='Mata pelajaran bahasa Indonesia', grade_level='SMA'),
        ]

        for subject in subjects:
            db.session.add(subject)
        db.session.commit()

        # Create admin user
        admin = User(
            username='admin',
            email='admin@lenteramu.id',
            full_name='Administrator',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)

        # Create teacher users
        teachers = [
            {'username': 'guru_matematika', 'email': 'guru.mtk@lenteramu.id',
                'full_name': 'Dr. Siti Nurhaliza', 'subjects': ['MTK']},
            {'username': 'guru_fisika', 'email': 'guru.fis@lenteramu.id',
                'full_name': 'Prof. Ahmad Dahlan', 'subjects': ['FIS']},
            {'username': 'guru_kimia', 'email': 'guru.kim@lenteramu.id',
                'full_name': 'Dra. Maya Sari', 'subjects': ['KIM']},
        ]

        for teacher_data in teachers:
            teacher = User(
                username=teacher_data['username'],
                email=teacher_data['email'],
                full_name=teacher_data['full_name'],
                role='guru'
            )
            teacher.set_password('guru123')
            db.session.add(teacher)
            db.session.commit()

            # Create teacher profile
            teacher_profile = TeacherProfile(
                user_id=teacher.id,
                teacher_id=f"TCH{teacher.id:03d}",
                school_name='SMA Negeri 1 Jakarta',
                subjects=json.dumps(teacher_data['subjects']),
                experience_years=5
            )
            db.session.add(teacher_profile)

        # Create student users
        students = [
            {'username': 'ahmad_rizki', 'email': 'ahmad.rizki@student.id',
                'full_name': 'Ahmad Rizki Pratama', 'grade': 'XI'},
            {'username': 'siti_aisyah', 'email': 'siti.aisyah@student.id',
                'full_name': 'Siti Aisyah Putri', 'grade': 'XI'},
            {'username': 'budi_santoso', 'email': 'budi.santoso@student.id',
                'full_name': 'Budi Santoso', 'grade': 'XII'},
            {'username': 'maya_indira', 'email': 'maya.indira@student.id',
                'full_name': 'Maya Indira Sari', 'grade': 'X'},
            {'username': 'rizki_fadillah', 'email': 'rizki.fadillah@student.id',
                'full_name': 'Rizki Fadillah', 'grade': 'XI'},
        ]

        for student_data in students:
            student = User(
                username=student_data['username'],
                email=student_data['email'],
                full_name=student_data['full_name'],
                role='siswa'
            )
            student.set_password('siswa123')
            db.session.add(student)
            db.session.commit()

            # Create student profile
            student_profile = StudentProfile(
                user_id=student.id,
                student_id=f"STD{student.id:04d}",
                grade_level=student_data['grade'],
                school_name='SMA Negeri 1 Jakarta',
                learning_style=['visual', 'auditory',
                                'kinesthetic'][student.id % 3],
                learning_pace=['normal', 'fast', 'slow'][student.id % 3],
                preferred_subjects=json.dumps(['MTK', 'FIS'])
            )
            db.session.add(student_profile)

        db.session.commit()

        # Create courses
        courses = [
            {'title': 'Aljabar Linear', 'subject_code': 'MTK',
                'difficulty': 'intermediate', 'type': 'video', 'duration': 45},
            {'title': 'Kalkulus Diferensial', 'subject_code': 'MTK',
                'difficulty': 'advanced', 'type': 'article', 'duration': 60},
            {'title': 'Geometri Ruang', 'subject_code': 'MTK',
                'difficulty': 'beginner', 'type': 'practice', 'duration': 30},
            {'title': 'Mekanika Newton', 'subject_code': 'FIS',
                'difficulty': 'intermediate', 'type': 'video', 'duration': 50},
            {'title': 'Gelombang dan Optik', 'subject_code': 'FIS',
                'difficulty': 'advanced', 'type': 'quiz', 'duration': 25},
            {'title': 'Ikatan Kimia', 'subject_code': 'KIM',
                'difficulty': 'beginner', 'type': 'video', 'duration': 40},
        ]

        for course_data in courses:
            subject = Subject.query.filter_by(
                code=course_data['subject_code']).first()
            course = Course(
                title=course_data['title'],
                description=f"Materi pembelajaran {course_data['title']}",
                subject_id=subject.id,
                difficulty_level=course_data['difficulty'],
                content_type=course_data['type'],
                content_url=f"/content/{course_data['title'].lower().replace(' ', '_')}",
                duration_minutes=course_data['duration']
            )
            db.session.add(course)

        db.session.commit()

        # Create student progress records
        students = StudentProfile.query.all()
        courses = Course.query.all()

        for student in students:
            # Each student progresses in first 4 courses
            for i, course in enumerate(courses[:4]):
                progress = StudentProgress(
                    student_id=student.id,
                    course_id=course.id,
                    progress_percentage=min(
                        100, (i + 1) * 25 + (student.id * 5)),
                    grade=['A', 'B', 'A', 'B+'][i] if i < 3 else None
                )
                db.session.add(progress)

        # Create AI recommendations
        for student in students:
            for course in courses[2:5]:  # Recommend courses 3-5 to each student
                recommendation = AIRecommendation(
                    user_id=student.user_id,
                    course_id=course.id,
                    recommendation_type='content',
                    match_score=85.0 + (student.id * 2),
                    reasoning=f"Based on learning style and previous performance"
                )
                db.session.add(recommendation)

        # Create system metrics
        metrics = [
            {'name': 'active_users', 'value': 234, 'unit': 'count'},
            {'name': 'cpu_usage', 'value': 45.2, 'unit': 'percentage'},
            {'name': 'memory_usage', 'value': 68.5, 'unit': 'percentage'},
            {'name': 'response_time', 'value': 120, 'unit': 'ms'},
            {'name': 'model_accuracy', 'value': 94.2, 'unit': 'percentage'},
        ]

        for metric_data in metrics:
            metric = SystemMetrics(
                metric_name=metric_data['name'],
                metric_value=metric_data['value'],
                metric_unit=metric_data['unit']
            )
            db.session.add(metric)

        # Create user feedback
        for student in students[:3]:  # First 3 students give feedback
            feedback = UserFeedback(
                user_id=student.user_id,
                feedback_type='system',
                rating=5,
                comments='Sistem sangat membantu dalam pembelajaran'
            )
            db.session.add(feedback)

        db.session.commit()
        print("Sample data created successfully!")


if __name__ == '__main__':
    init_database()
