import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fender-stomp-duffel-sort-hotspot-gabled'