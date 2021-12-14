from flask import Blueprint

blueprint = Blueprint(
    'util',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)