from os import environ
from sys import exit
# from flask_migrate import Migrate
from config import config_dict
from app import create_app
# from app.base.models import User, Roles


get_config_mode = environ.get('CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except:
    exit('Error: Invalid CONFIG_MODE environment variable.')
    
app = create_app(config_mode)
#Migrate(app, db, render_as_batch=True)

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Role': Roles}
