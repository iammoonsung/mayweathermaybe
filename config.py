import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'open-sesame'
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
        user='root', password='1234',
        database='mayweather')
    SQLALCHEMY_TRACK_MODIFICATIONS = False