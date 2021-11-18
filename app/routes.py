from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.jinja", title="Main")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.jinja', title='Sign In', form=form)

@app.route('/student/')
@app.route('/student/<name>')
def student(name=None):
    if name is None:
        name = "Unknown"
    return render_template("student.jinja", title="Student Page", name=name)

@app.route('/career')
def career():
    return "Not Implemented"