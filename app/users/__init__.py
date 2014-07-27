# -*- coding: utf-8 -*-
"""
    app.users
    ~~~~~~~~~~~~~~

    app users package
"""
from flask import Blueprint

users = Blueprint('users', __name__)

from .models import User