import os
#import json
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Testing-this-app-causes-me-headaches'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER= os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #ADMINS = json.loads(os.environ['ADMINS'])
    

class ProductionConfig(Config):
    DEBUG = False
    
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    
    # PostgresSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('DATABASE_USER'),
        os.environ.get('DATABASE_PASSWORD'),
        os.environ.get('DATABASE_HOST'),
        os.environ.get('DATABASE_PORT', 5432),
        os.environ.get('DATABASE_NAME')
    )


class DebugConfig(Config):
    DEBUG = True
    
    
class TestingConfig(Config):
    DEBUG=True
    
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
    'Testing': TestingConfig
}