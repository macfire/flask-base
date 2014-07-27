flask-base
==========

Flask-Base is a starter template for my Flask-based apps.

I am new to Python and Flask, so this repository is a work-in-progress. 
Updates will be made as I learn 'best-practices' from [others](#credits) and determine what works best for my style.


#####Notes
* Blueprint placeholder included as reference
* Flask-User in requirements file
* TextMate project file
* css, js, and image placeholders

[Credits](#credits)


***

####Structure

    - flask-base
    |- config.py
    |- manage.py
    |- app
      |- __init__.py (create_app())
      |- blueprint-1 (placeholder)
      |- static
        |- css
        |- images
        |- js
      |- templates
        |- blueprint-1
        |- user (for blueprint or Flask-User)
    |- requirements
    |- tests

***

####Code Reminders

To clone to new folder

    git clone git@github.com:macfire/flask-base.git your-new-app-folder-name

Create virtual environment

    user:~/flask-base 
    $ virtualenv venv

Activate virtual environment

    user:~/flask-base 
    $ source venv/bin/activate

pip install required packages (edit requirements as necessary)

    (venv) $ pip install -r requirements/dev.txt

Create database

    (venv) $ python manage.py shell
    >>> from app import db
    >>> db.create_all()

Generate requirements

    (venv) $ pip freeze >requirements/common.txt

Make manage.py executable

    (venv) $ chmod a+x manage.py
    Note: file must begin with #!/usr/bin/env python

Using Flask-Migrate

    (venv) $ ./manage.py db init
    (venv) $ ./manage.py db migrate -m "initial migration"
    (venv) $ ./manage.py db upgrade

***

####Credits

Structure and scripts pulled from various sources, including: 

* http://www.flaskbook.com
* https://github.com/miguelgrinberg/flasky
* http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* http://maximebf.com/blog/2012/11/getting-bigger-with-flask/
* http://pythonthusiast.pythonblogs.com/230_pythonthusiast/archive/1369_flask_biography_tutorial_part_xiv-redesign_the_application_using_blueprints.html
* https://github.com/mattupstate/overholt

