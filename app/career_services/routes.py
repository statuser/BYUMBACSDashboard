from app.career_services import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('cs/dashboard.jinja')