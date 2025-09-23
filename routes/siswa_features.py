from flask import Blueprint, render_template, session
from ai.learning_process import create_ai_learning_process

siswa_features_bp = Blueprint(
    'siswa_features', __name__, url_prefix='/siswa/features')

# --- Task List ---


@siswa_features_bp.route('/tugas')
def tugas():
    """Daftar tugas siswa (dinamis, sinkron dengan Course dan progress demo)"""
    from models import StudentProfile, Course, StudentProgress
    user_id = session.get('user_id')
    tugas_list = []
    if user_id:
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if student:
            tugas_courses = Course.query.filter_by(
                content_type='practice').all()
            for t in tugas_courses:
                progress = StudentProgress.query.filter_by(
                    student_id=student.id, course_id=t.id).first()
                tugas_list.append({
                    'id': t.id,
                    'judul': t.title,
                    'deadline': '-',
                    'status': f"{progress.progress_percentage if progress else 0}%",
                })
    return render_template('siswa/fitur_siswa_tugas.html', tugas_list=tugas_list)

# --- Quiz List ---


@siswa_features_bp.route('/kuis')
def kuis():
    """Daftar kuis siswa (dinamis, sinkron dengan Course dan progress demo)"""
    from models import StudentProfile, Course, StudentProgress
    user_id = session.get('user_id')
    kuis_list = []
    if user_id:
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if student:
            kuis_courses = Course.query.filter_by(content_type='quiz').all()
            for k in kuis_courses:
                progress = StudentProgress.query.filter_by(
                    student_id=student.id, course_id=k.id).first()
                kuis_list.append({
                    'id': k.id,
                    'judul': k.title,
                    'durasi': k.duration_minutes if hasattr(k, 'duration_minutes') else 30,
                    'status': f"{progress.progress_percentage if progress else 0}%",
                })
    return render_template('siswa/fitur_siswa_kuis.html', kuis_list=kuis_list)

# --- Materi List ---


@siswa_features_bp.route('/materi')
def materi():
    """Daftar materi siswa (dinamis, sinkron dengan Course dan progress demo)"""
    from models import StudentProfile, Course, StudentProgress
    user_id = session.get('user_id')
    materi_list = []
    if user_id:
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if student:
            materi_courses = Course.query.filter_by(
                content_type='article').all()
            for m in materi_courses:
                progress = StudentProgress.query.filter_by(
                    student_id=student.id, course_id=m.id).first()
                materi_list.append({
                    'id': m.id,
                    'judul': m.title,
                    'deskripsi': m.description or '',
                    'status': f"{progress.progress_percentage if progress else 0}%",
                })
    return render_template('siswa/fitur_siswa_materi.html', materi_list=materi_list)


siswa_features_bp = Blueprint(
    'siswa_features', __name__, url_prefix='/siswa/features')

# --- Guidelines ---


@siswa_features_bp.route('/guidelines')
def guidelines():
    """Halaman panduan lengkap fitur, AI, RL, dan cara kerja untuk siswa"""
    return render_template('siswa/guidelines.html')

# --- AI Recommendation ---


@siswa_features_bp.route('/rekomendasi')
def ai_rekomendasi():
    """Rekomendasi AI (Q-learning + CBF) untuk siswa"""
    user_id = session.get('user_id')
    if not user_id:
        return render_template('siswa/fitur_siswa_rekomendasi.html', rekomendasi_list=[])
    from models import StudentProfile
    student = StudentProfile.query.filter_by(user_id=user_id).first()
    if not student:
        return render_template('siswa/fitur_siswa_rekomendasi.html', rekomendasi_list=[])
    ai_learning = create_ai_learning_process()
    rekomendasi_list = ai_learning.generate_recommendations(student.id)
    print('DEBUG REKOMENDASI:', rekomendasi_list)
    return render_template('siswa/fitur_siswa_rekomendasi.html', rekomendasi_list=rekomendasi_list)

# --- Task & Notification ---


@siswa_features_bp.route('/notifications')
def notifications():
    """Notifikasi tugas, deadline, pengumuman (Siswa)"""
    from models import StudentProfile, StudentProgress
    user_id = session.get('user_id')
    notifications = []
    if user_id:
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if student:
            # Dummy: notifikasi tugas belum selesai, nilai keluar, pengumuman
            progress = StudentProgress.query.filter_by(
                student_id=student.id).all()
            for p in progress:
                if p.progress_percentage < 100:
                    notifications.append(
                        {'type': 'assignment', 'message': f'Tugas {p.course_id} belum selesai', 'time': 'Hari ini'})
                if p.grade:
                    notifications.append(
                        {'type': 'grade', 'message': f'Nilai tugas {p.course_id}: {p.grade}', 'time': 'Kemarin'})
            notifications.append(
                {'type': 'announcement', 'message': 'Jadwal ujian telah diumumkan.', 'time': '2 hari lalu'})
    return render_template('siswa/notifications.html', notifications=notifications)

# --- Personal Analytics ---


@siswa_features_bp.route('/analytics')
def personal_analytics():
    """Analitik pembelajaran pribadi (Siswa)"""
    from models import StudentProfile, StudentProgress, LearningActivity, Subject
    import json
    user_id = session.get('user_id')
    chart_labels = []
    chart_data = []
    nilai_list = []
    if user_id:
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if student:
            progress = StudentProgress.query.filter_by(
                student_id=student.id).all()
            for p in progress:
                # Label: nama materi/tugas/kuis dari Course
                label = p.course.title if p.course else f"ID {p.course_id}"
                chart_labels.append(label)
                chart_data.append(int(p.progress_percentage))
                # Nilai detail
                nilai_list.append({
                    'mata_pelajaran': label,
                    'nilai': p.grade or '-'
                })
    return render_template(
        'siswa/fitur_siswa_analitik.html',
        chart_labels=json.dumps(chart_labels),
        chart_data=json.dumps(chart_data),
        nilai_list=nilai_list
    )

# --- AI Interest Recommendation ---


@siswa_features_bp.route('/ai-interest')
def ai_interest():
    """Rekomendasi AI berbasis minat & kelemahan (Siswa)"""
    return render_template('siswa/ai_interest.html')

# --- Discussion/Community ---


@siswa_features_bp.route('/community')
def community():
    """Fitur diskusi/komunitas (Siswa)"""
    return render_template('siswa/community.html')

# --- Progress Badge ---


@siswa_features_bp.route('/badges')
def badges():
    """Progress badge/achievement (Siswa)"""
    from models import StudentProfile, User, StudentProgress
    user_id = session.get('user_id')
    badges = []
    if user_id:
        student = StudentProfile.query.filter_by(user_id=user_id).first()
        if student:
            # Contoh badge: progress, streak, nilai, dsb
            progress = StudentProgress.query.filter_by(
                student_id=student.id).all()
            completed = len(
                [p for p in progress if p.progress_percentage == 100])
            badges = [
                {'icon': 'fa-graduation-cap', 'name': 'Penyelesai Materi',
                    'desc': 'Selesaikan 1 materi/tugas', 'unlocked': completed >= 1},
                {'icon': 'fa-star', 'name': 'Bintang Belajar',
                    'desc': 'Selesaikan 5 materi/tugas', 'unlocked': completed >= 5},
                {'icon': 'fa-fire', 'name': 'Streak Konsisten',
                    'desc': 'Belajar 3 hari berturut-turut', 'unlocked': False},
                {'icon': 'fa-trophy', 'name': 'Nilai Hebat',
                    'desc': 'Rata-rata nilai > 85', 'unlocked': False},
            ]
    return render_template('siswa/badges.html', badges=badges)

# --- Exam Simulation ---


@siswa_features_bp.route('/tryout')
def tryout():
    """Simulasi ujian/tryout (Siswa)"""
    return render_template('siswa/tryout.html')

# --- Learning Calendar ---


@siswa_features_bp.route('/calendar')
def calendar():
    """Integrasi kalender belajar (Siswa)"""
    return render_template('siswa/calendar.html')

# --- AI Feedback ---


@siswa_features_bp.route('/ai-feedback')
def ai_feedback():
    """Feedback AI untuk materi/latihan (Siswa)"""
    return render_template('siswa/ai_feedback.html')
