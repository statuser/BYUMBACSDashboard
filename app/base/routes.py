from flask import render_template
from app import login_manager
from app.base import blueprint


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template("index.jinja", title="Main")

# Error Pages

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500