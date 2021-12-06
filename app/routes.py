from flask import render_template, flash, redirect, url_for
from wtforms.fields.simple import TextAreaField
from app import app, db
from app.models import Student




@app.route('/')
@app.route('/index')
def index():
    return render_template("index.jinja", title="Main")

@app.route("/student")
@app.route('/student/<int:studentId>')
def student(studentId=None):
    # Load the student data from the database
    student = Student.query.get(studentId)
    if not student:
        flash('Student ID Does not exist')
        return redirect(url_for('index'))
    # Send the data to webpage to render
    return render_template("student.jinja", title='Student Page', student=student)

#Team Garam code for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.jinja', error=error)

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
def career():
    return "Not Implemented"

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
                          profileImage=form.profileImage.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('newStudent.jinja', title='New Student', form=form)
