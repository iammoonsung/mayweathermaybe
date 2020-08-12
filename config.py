import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'open-sesame'
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@13.125.205.2:3306/{database}').format(
        user='root', password='testtest',
        database='mayweather')
    SQLALCHEMY_TRACK_MODIFICATIONS = False