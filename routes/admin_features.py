
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User


admin_features_bp = Blueprint(
    'admin_features', __name__, url_prefix='/admin/features')

# --- User Management ---


@admin_features_bp.route('/users', methods=['GET'])
def manage_users():
    """CRUD Manajemen User (Admin)"""
    users = User.query.order_by(User.created_at.desc()).all()
    if not users:
        # Buat data demo jika user kosong
        demo_users = [
            User(username='admin', email='admin@lenteramu.id',
                 full_name='Demo Admin', role='admin', is_active=True),
            User(username='guru1', email='guru1@lenteramu.id',
                 full_name='Guru Satu', role='guru', is_active=True),
            User(username='siswa1', email='siswa1@lenteramu.id',
                 full_name='Siswa Satu', role='siswa', is_active=True),
        ]
        for u in demo_users:
            u.set_password('demo123')
            db.session.add(u)
        db.session.commit()
        users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/manage_users.html', users=users)

# --- Class & Subject Management ---


@admin_features_bp.route('/classes')
def manage_classes():
    """Manajemen Kelas & Mata Pelajaran (Admin)"""
    return render_template('admin/manage_classes.html')

# --- AI Model Monitoring ---


@admin_features_bp.route('/ai-monitor')
def ai_monitor():
    """Monitoring performa AI model (Admin)"""
    return render_template('admin/ai_monitor.html')

# --- System Notification ---


@admin_features_bp.route('/notifications')
def system_notifications():
    """Notifikasi sistem & broadcast (Admin)"""
    return render_template('admin/system_notifications.html')

# --- Export Data ---


@admin_features_bp.route('/export')
def export_data():
    """Export data (Admin)"""
    return render_template('admin/export_data.html')

# --- Audit Log ---


@admin_features_bp.route('/audit-log')
def audit_log():
    """Audit log aktivitas admin"""
    return render_template('admin/audit_log.html')

# --- Real-time Dashboard ---


@admin_features_bp.route('/realtime-dashboard')
def realtime_dashboard():
    """Dashboard real-time interaktif (Admin)"""
    return render_template('admin/realtime_dashboard.html')
