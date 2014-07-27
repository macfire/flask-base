# -*- coding: utf-8 -*-
"""
    app.config
    ~~~~~~~~~~~~~~~

    app config module
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    CSRF_ENABLED = True

    # SQLALCHEMY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Flask-Mail -- Required for Confirm email and Forgot password features
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    #MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = '"Sender" <noreply@example.com>'

    # Configure Flask-User
    USER_ENABLE_USERNAME        = True              # Register and Login with username
    USER_ENABLE_EMAIL           = True              # Register with email
    USER_ENABLE_CONFIRM_EMAIL   = True              # Require email confirmation
    USER_ENABLE_CHANGE_USERNAME = True
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_ENABLE_FORGOT_PASSWORD = True


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
