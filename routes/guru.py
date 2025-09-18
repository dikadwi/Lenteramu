from flask import Blueprint, render_template, session
from models import db
from ai.learning_process import create_ai_learning_process

guru_bp = Blueprint('guru', __name__, url_prefix='/guru')


@guru_bp.route('/dashboard')
def dashboard_guru():
    user = {
        'name': session.get('user_name', 'Demo Teacher'),
        'role': session.get('user_role', 'teacher'),
        'email': session.get('username', 'guru@lenteramu.id'),
        'avatar': session.get('avatar', '/static/images/avatar-teacher.png'),
        'subject': session.get('subject', 'Matematika'),
        'employee_id': session.get('employee_id', 'TCH2024001'),
        'join_date': session.get('join_date', '2020-08-01'),
    }
    context = {
        'user': user,
        'teacher_name': user.get('name', 'Demo Teacher'),
        'user_role': 'teacher',
    }
    return render_template('guru/dashboard_guru.html', **context)
