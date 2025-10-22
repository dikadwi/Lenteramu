from flask import Blueprint, render_template
from utils.decorators import public_route

# Create blueprint
cara_kerja = Blueprint('cara_kerja', __name__, url_prefix='/cara_kerja')


# Cara Kerja routes (now use subfolders for each role)
@cara_kerja.route('/siswa')
@public_route
def cara_kerja_siswa():
    return render_template('landing_page/cara_kerja/siswa.html')


@cara_kerja.route('/guru')
@public_route
def cara_kerja_guru():
    return render_template('landing_page/cara_kerja/guru.html')


@cara_kerja.route('/admin')
@public_route
def cara_kerja_admin():
    return render_template('landing_page/cara_kerja/admin.html')


@cara_kerja.route('/analytics')
@public_route
def cara_kerja_analytics():
    return render_template('landing_page/cara_kerja/analytics.html')
