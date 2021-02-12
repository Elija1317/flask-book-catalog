
#/app/__init__

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



#created database instance
db = SQLAlchemy()
#create instance of Bootstrap
bootsrap = Bootstrap()
loginmanger = LoginManager()
loginmanger.login_view = 'authentication.do_the_login'
loginmanger.session_protection = 'strong'
bycrpt = Bcrypt()


# create app to run the pythong files, before we are declaring if __name__ == 'main':
#app.run(debug =True)

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(),'config',config_type + '.py')
    #'C:\\Users\\rgone4\\PycharmProjects\\book_catlog\\config\\dev.py'
    app.config.from_pyfile(configuration)
    # pass the db instance to app
    db.init_app(app)
    bootsrap.init_app(app) #intialse the boot strap
    loginmanger.init_app(app)
    bycrpt.init_app(app)


    #import the instance of blue print which is written in catalog/__init__.py
    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app



