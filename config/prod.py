import os

DEBUG = False
SECRET_KEY = 'topscret'
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:qwer@localhost/catlog_db'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False