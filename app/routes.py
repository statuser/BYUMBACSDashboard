from flask import render_template
from wtforms.fields.simple import TextAreaField
from app import app
from flask import Flask, render_template, redirect, url_for, request





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