from flask import render_template
from . import blueprint_1

@blueprint_1.route('/')
def index():
    return render_template('blueprint_1/base.html')