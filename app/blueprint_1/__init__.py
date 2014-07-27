from flask import Blueprint

blueprint_1 = Blueprint('blueprint_1', __name__)

from . import views