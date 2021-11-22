from flask import render_template
from app import app

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
    return render_template("student.jinja", title="Student Page", student=student)

@app.route('/career')
def career():
    return "Not Implemented"