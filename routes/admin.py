from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from models import db, User, SystemMetrics, LearningActivity
from ai.learning_process import create_ai_learning_process

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
ai_learning_process = create_ai_learning_process()


@admin_bp.route('/dashboard')
def dashboard_admin():
    user = {
        'name': session.get('user_name', 'Demo Admin'),
        'role': session.get('user_role', 'admin'),
        'email': session.get('username', 'admin@lenteramu.id'),
        'avatar': session.get('avatar', '/static/images/avatar-admin.png'),
        'department': session.get('department', 'IT Administration'),
        'employee_id': session.get('employee_id', 'ADM2024001'),
        'join_date': session.get('join_date', '2019-03-15'),
    }
    context = {
        'user': user,
        'admin_name': user.get('name', 'Demo Admin'),
        'user_role': 'admin',
        'system_metrics': {
            'cpu_usage': 35,
            'memory_usage': 62,
            'disk_usage': 48,
            'network_traffic': '120 MB/s',
        },
    }
    return render_template('admin/dashboard_admin.html', **context)


@admin_bp.route('/workflow')
def admin_workflow():
    user = {
        'name': session.get('user_name', 'Demo Admin'),
        'role': session.get('user_role', 'admin'),
        'email': session.get('username', 'admin@lenteramu.id'),
    }
    try:
        total_users = User.query.count()
        active_users = User.query.filter_by(is_active=True).count()
        system_metrics = SystemMetrics.query.order_by(
            SystemMetrics.recorded_at.desc()).limit(10).all()
        recent_activities = LearningActivity.query.order_by(
            LearningActivity.created_at.desc()).limit(20).all()
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
        workflow_data['user'] = user
        return render_template('workflows/admin_workflow.html', **workflow_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
