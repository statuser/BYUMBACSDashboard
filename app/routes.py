from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewStudentForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.jinja", title="Main")

@app.route("/student")
@app.route('/student/<studentID>')
def student(studentId = 0):
    # Load the student data from the database
    # student = load student from database
    student = {
        'firstName' : 'Sophie',
        'lastName' : 'Rose',
        'class' : '2022',
        'track' : 'Marketing',
        'mentor' : 'Jon Kent',
        'interest' : 'Tech',
        'profileImage' : 'https://source.unsplash.com/Av_NirIguEc/600x600'
    }
    # Send the data to webpage to render
    return render_template("student.jinja", title='Student Page', student=student)

@app.route('/career')
def career():
    return "Not Implemented"

@app.route('/create_student', methods=['GET', 'POST'])
def create_student():
    form = NewStudentForm()
    if form.validate_on_submit():
        flash(f'Create New Student Requested for {form.firstName.data} {form.lastName.data}')
        return redirect(url_for('index'))
    return render_template('newStudent.jinja', title='New Student', form=form)
