import os
import logging
from importlib import import_module
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'util.login'
login_manager.login_message = 'Please log in to access this page.'
bootstrap = Bootstrap()
mail = Mail()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    

def register_blueprints(app):
    for module_name in ('base', 'career_services', 'students', 'util'):
        module = import_module(f'app.{module_name}.routes')
        app.register_blueprint(module.blueprint)


def configure_database(app):
    
    @app.before_first_request
    def initialize_database():
        db.create_all()
        
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()
        
        

def configure_logs(app):
    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='CSDashboard Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
    
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/csdashboard.log', maxBytes=10240,
                                        backupCount=10)
        file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('CSDashboard startup')
    
    
def create_app(config_class=Config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config_class)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)
    return app



from app.base import models