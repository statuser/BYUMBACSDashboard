from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.jinja", title="Main")

@app.route('/student')
def student():
    return "Not Implemented"

@app.route('/career')
def career():
    return "Not Implemented"