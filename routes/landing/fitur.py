from flask import Blueprint, render_template
from utils.decorators import public_route

# Create blueprint
fitur = Blueprint('fitur', __name__, url_prefix='/fitur')


@fitur.route('/ai-learning')
@public_route
def ai_learning():
    return render_template('landing_page/fitur/ai_learning.html')


@fitur.route('/realtime_analytics')
@public_route
def realtime_analytics():
    return render_template('landing_page/fitur/realtime_analytics.html')


@fitur.route('/adaptive-feedback')
@public_route
def adaptive_feedback():
    return render_template('landing_page/fitur/adaptive_feedback.html')


@fitur.route('/multi-role')
@public_route
def multi_role():
    return render_template('landing_page/fitur/multi_role.html')
