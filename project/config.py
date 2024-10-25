import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a6b12576aa095f14d7ae29f5')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False