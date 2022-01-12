from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user

from app import db
from app.base.routes import access_forbidden
from app.base.models import Student, StudentNote

from app.students import blueprint
from app.students.forms import IntakeSurvey, KPIForm, EditStudentProfileForm

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

@blueprint.route('/edit_profile/<studentId>', methods=['GET', 'POST'])
@blueprint.route('/edit_profile/', methods=['GET', 'POST'])
@login_required
def edit_profile(studentId=None):
    if studentId is None:
        studentId = current_user.student
    
    student = Student.query.get(studentId) or abort(404)
    
    form = EditStudentProfileForm()
    if form.validate_on_submit():
        # Does not Check for duplicates need to add a unique key for this.  Maybe Email?
        student.firstName=form.firstName.data,
        student.lastName=form.lastName.data,
        student.classYear=form.classYear.data,
        student.track=form.track.data,
        student.mentor=form.mentor.data,
        student.interest=form.interest.data,
        student.profileImagePath=form.profileImage.data
        db.session.commit(student)
        flash('Your changes have been saved.')
        return redirect(url_for('students.dashboard'))
    elif request.method == 'GET':
        form.firstName.data = student.firstName
        form.lastName.data = student.lastName
        form.classYear.data = student.classYear
        form.track.data = student.track
        form.mentor.data = student.mentor
        form.interest.data = student.interest
        form.profileImage.data = student.profileImage
    return render_template("students/edit_profile.jinja", title="Edit My Profile", form=form)

@blueprint.route('/create_student', methods=['GET', 'POST'])
def create_student():
    form = EditStudentProfileForm()
    if form.validate_on_submit():
        # Does not Check for duplicates need to add a unique key for this.  Maybe Email?
        student = Student(firstName=form.firstName.data,
                          lastName=form.lastName.data,
                          classYear=form.classYear.data,
                          track=form.track.data,
                          mentor=form.mentor.data,
                          interest=form.interest.data,
                          profileImagePath=form.profileImage.data)
        db.session.add(student)
        db.session.commit()
        flash('The student has been created')
        return redirect(url_for('students.dashboard'))
    return render_template("students/newStudent.jinja", title="Create Student", form=form)