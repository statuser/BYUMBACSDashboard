from app.career_services import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('cs/dashboard.jinja')

@blueprint.route('/student_view')
@login_required
def student_view():
    return render_template('cs/student_view.jinja')