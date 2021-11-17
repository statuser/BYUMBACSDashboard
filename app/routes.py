from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.jinja", title="Main")

@app.route('/student/<name>')
def student(name):
    
    return render_template("student.jinja", title="Student Page", name=name)

@app.route('/career')
def career():
    return "Not Implemented"