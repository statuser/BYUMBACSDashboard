from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.base.routes import access_forbidden
from app.base.models import Student, StudentNote

from app.students import blueprint
from app.students.forms import IntakeSurvey, KPIForm

@blueprint.route('/intake_survey', methods=['GET', 'POST'])
@login_required
def intake_survey():
    form = IntakeSurvey()
    if form.validate_on_submit():
        # Does not Check for duplicates need to add a unique key for this.  Maybe Email?
        # student = ...
        student = Student()
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('base.index'))
    return render_template('students/intake_survey.jinja', title='Intake Survey', form=form)

@blueprint.route('/kpi_reporting', methods=['GET', 'POST'])
@login_required
def kpi_reporting():
    form = KPIForm()
    if form.validate_on_submit():
        # Does not Check for duplicates need to add a unique key for this.  Maybe Email?
        #student = Student()
        #db.session.add(student)
        #db.session.commit()
        return redirect(url_for('base.index'))
    return render_template('students/kpi_reporting.jinja', title='Weekly KPI Report', form=form)
	
@blueprint.route('/dashboard')
@login_required
def dashboard():
    # if not current_user.student:
    #     access_forbidden('You must be a current student to access this page!')
    student = {
        'photo' : 'https://slc.byu.edu/sites/saltlakecenter.ce.byu.edu/files/current_students.png',
        'firstName' : 'Nathan',
        'lastName' : 'Saguibo',
        'class' : '2023',
        'track' : 'Marketing',
        'mentor' : 'Jon Kent',
        'interest' : 'Tech'
    }
    
    return render_template("students/dashboard.jinja", student=student, title="Main")

@blueprint.route('/edit_profile')
@login_required
def edit_profile():
    return render_template("students/edit_profile.jinja", title="Main")