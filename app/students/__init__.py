from flask import Blueprint

blueprint = Blueprint(
    'students',
    __name__,
    url_prefix='/students',
    template_folder='templates',
    static_folder='static'
)