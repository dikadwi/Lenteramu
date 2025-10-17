from flask import Blueprint, render_template
from utils.decorators import public_route

# Create blueprint
legal = Blueprint('legal', __name__, url_prefix='/legal')


@legal.route('/privacy')
@public_route
def privacy():
    return render_template('landing_page/legal/privacy_policy.html')


@legal.route('/terms')
@public_route
def terms():
    return render_template('landing_page/legal/terms.html')


@legal.route('/cookies')
@public_route
def cookies():
    return render_template('landing_page/legal/cookies.html')
