from os import name
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.models import User, Student
from app.forms import LoginForm, NewStudentForm, WeeklyReportForm





@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.jinja", title="Main")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('student'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.jinja', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/student/<int:studentId>')
@app.route('/student')
@login_required
def student(studentId = 0):
    # Load the student data from the database
    student = Student.query.get(studentId)
    if not student:
        flash('Student ID Does not exist')
        return redirect(url_for('index'))
    return render_template("student.jinja", title='Student Page', student=student)

@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('forgotpassword.jinja', error=error)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('reset.jinja', error=error)

    #team garam  page

@app.route('/career')
@login_required
def career():
    return render_template('careerServices.jinja')

@app.route('/create_student', methods=['GET', 'POST'])
def create_student():
    form = NewStudentForm()
    if form.validate_on_submit():
        # Does not Check for duplicates need to add a unique key for this.  Maybe Email?
        student = Student(firstName=form.firstName.data,
                          lastName=form.lastName.data,
                          classYear=form.classYear.data,
                          track=form.track.data,
                          mentor=form.mentor.data,
                          interest=form.interest.data,
                          profileImage=form.profileImage.data,
                          email=form.email.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('newStudent.jinja', title='New Student', form=form)

@app.route('/weekly_report', methods=['GET', 'POST'])
def weekly_report():
    form = WeeklyReportForm()
    if form.validate_on_submit():
        # Does not Check for duplicates need to add a unique key for this.  Maybe Email?
        #student = Student()
        #db.session.add(student)
        #db.session.commit()
        return redirect(url_for('index'))
    return render_template('weeklyReport.jinja', title='Weekly Report', form=form)