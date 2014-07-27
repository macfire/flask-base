# -*- coding: utf-8 -*-
"""
    app.users.models
    ~~~~~~~~~~~~~~~~~~~~~

    User models
"""
from .. import db
from flask.ext.user import UserMixin
from . import users
#from ..helpers import JsonSerializer

# Define the User-Roles pivot table
user_roles = db.Table('user_roles',
        db.Column('id', db.Integer(), primary_key=True),
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE')))

    # Define Role model
class Role(db.Model):
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(50), unique=True)

    # Define User model. Make sure to add flask.ext.user UserMixin!!
class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=True, default=None)
        # Flask-User fields
        active = db.Column(db.Boolean(), nullable=False, default=False)
        email = db.Column(db.String(255), nullable=False, default='')
        password = db.Column(db.String(255), nullable=False, default='')
        # Relationships
        user_profile = db.relationship('UserProfile', uselist=False, foreign_keys=[user_profile_id])
        roles = db.relationship('Role', secondary=user_roles,
                backref=db.backref('users', lazy='dynamic'))

class UserProfile(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(50), nullable=False, default='')
        last_name = db.Column(db.String(50), nullable=False, default='')