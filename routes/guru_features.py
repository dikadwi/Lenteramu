from flask import Blueprint, render_template

guru_features_bp = Blueprint(
    'guru_features', __name__, url_prefix='/guru/features')

# --- Class Management ---


@guru_features_bp.route('/classes')
def manage_classes():
    """Manajemen kelas (Guru)"""
    return render_template('guru/manage_classes.html')

# --- Assignment & Quiz Scheduling ---


@guru_features_bp.route('/assignments')
def manage_assignments():
    """Penjadwalan & monitoring tugas/kuis (Guru)"""
    return render_template('guru/manage_assignments.html')

# --- Class Analytics ---


@guru_features_bp.route('/analytics')
def class_analytics():
    """Analitik kelas (Guru)"""
    return render_template('guru/class_analytics.html')

# --- AI Teaching Recommendation ---


@guru_features_bp.route('/ai-recommendation')
def ai_recommendation():
    """Rekomendasi AI untuk pengajaran (Guru)"""
    return render_template('guru/ai_recommendation.html')

# --- Auto Feedback ---


@guru_features_bp.route('/auto-feedback')
def auto_feedback():
    """Feedback otomatis untuk tugas/kuis (Guru)"""
    return render_template('guru/auto_feedback.html')

# --- Communication ---


@guru_features_bp.route('/communication')
def communication():
    """Komunikasi dengan siswa (Guru)"""
    return render_template('guru/communication.html')

# --- Student Notification ---


@guru_features_bp.route('/student-notifications')
def student_notifications():
    """Notifikasi aktivitas siswa (Guru)"""
    return render_template('guru/student_notifications.html')

# --- Export Report ---


@guru_features_bp.route('/export-report')
def export_report():
    """Export nilai & laporan kelas (Guru)"""
    return render_template('guru/export_report.html')
