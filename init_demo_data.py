"""
Script untuk mengisi data demo user, profil siswa, materi, tugas, progress, agar AI dan fitur siswa berjalan penuh.
Jalankan: python init_demo_data.py
"""
from models import db, User, StudentProfile, LearningActivity, StudentProgress, Course, Subject
from app import app
from datetime import datetime, timedelta


def create_demo_data():
    with app.app_context():
        # Demo user siswa
        user = User.query.filter_by(username='demo_student').first()
        if not user:
            user = User(
                username='demo_student',
                email='demo_student@lenteramu.id',
                full_name='Demo Siswa',
                role='siswa',
                is_active=True
            )
            user.set_password('demo123')
            db.session.add(user)
            db.session.commit()

        # Demo student profile
        student = StudentProfile.query.filter_by(user_id=user.id).first()
        if not student:
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
                engagement_level='medium',
                created_at=datetime.utcnow() - timedelta(days=30)
            )
            db.session.add(student)
            db.session.commit()

        # Demo subject
        subject = Subject.query.filter_by(code='MAT').first()
        if not subject:
            subject = Subject(name='Matematika', code='MAT',
                              description='Matematika Dasar', grade_level='XII')
            db.session.add(subject)
            db.session.commit()

        # Demo courses (materi, tugas, kuis)
        demo_courses = [
            {'title': 'Persamaan Linear',
                'description': 'Materi tentang Persamaan Linear', 'content_type': 'article'},
            {'title': 'Hukum Newton', 'description': 'Materi tentang Hukum Newton',
                'content_type': 'video'},
            {'title': 'Reaksi Kimia', 'description': 'Materi tentang Reaksi Kimia',
                'content_type': 'article'},
            {'title': 'Tugas Matematika 1',
                'description': 'Tugas latihan matematika', 'content_type': 'practice'},
            {'title': 'Tugas Fisika 1', 'description': 'Tugas latihan fisika',
                'content_type': 'practice'},
            {'title': 'Kuis Matematika',
                'description': 'Kuis matematika dasar', 'content_type': 'quiz'},
            {'title': 'Kuis Fisika', 'description': 'Kuis fisika dasar',
                'content_type': 'quiz'},
        ]
        course_ids = []
        for c in demo_courses:
            course = Course.query.filter_by(title=c['title']).first()
            if not course:
                course = Course(
                    title=c['title'],
                    description=c['description'],
                    subject_id=subject.id,
                    difficulty_level='beginner',
                    content_type=c['content_type'],
                    is_active=True
                )
                db.session.add(course)
                db.session.commit()
            course_ids.append(course.id)

        # Demo aktivitas belajar (LearningActivity)
        for i, course_id in enumerate(course_ids):
            la = LearningActivity.query.filter_by(
                user_id=user.id, course_id=course_id).first()
            if not la:
                la = LearningActivity(
                    user_id=user.id,
                    course_id=course_id,
                    activity_type='complete',
                    start_time=datetime.utcnow() - timedelta(days=10-i),
                    end_time=datetime.utcnow() - timedelta(days=9-i),
                    score=85.0,
                    completed=True
                )
                db.session.add(la)
        db.session.commit()

        # Demo progress siswa
        for course_id in course_ids:
            progress = StudentProgress.query.filter_by(
                student_id=student.id, course_id=course_id).first()
            if not progress:
                progress = StudentProgress(
                    student_id=student.id,
                    course_id=course_id,
                    progress_percentage=100,
                    grade='85',
                    created_at=datetime.utcnow() - timedelta(days=10)
                )
                db.session.add(progress)
        db.session.commit()

        print('Data demo berhasil diisi!')


if __name__ == '__main__':
    create_demo_data()
