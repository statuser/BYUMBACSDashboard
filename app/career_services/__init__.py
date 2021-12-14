from flask import Blueprint

blueprint = Blueprint(
    'career_services',
    __name__,
    url_prefix='/cs',
    template_folder='templates',
    static_folder='static'
)