# -*- coding: utf-8 -*-
"""
    app.__init__
"""

from flask import Flask
#from flask.ext.bootstrap import Bootstrap
#from flask.ext.mail import Mail
#from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager
#from flask.ext.pagedown import PageDown
from config import config

#bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
db = SQLAlchemy()
#pagedown = PageDown()

# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #bootstrap.init_app(app)
    #mail.init_app(app)
    #moment.init_app(app)
    db.init_app(app)
    #login_manager.init_app(app)
    #pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .blueprint_1 import blueprint_1 as blueprint_1_blueprint
    app.register_blueprint(blueprint_1_blueprint, url_prefix='/blueprint_1')

    return app
