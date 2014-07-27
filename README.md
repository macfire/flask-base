flask-base
==========

Starter template for Flask-based apps. Blueprint placeholders are included as reference and to help spin up new project. 
TextMate project file included. 

[Credits](#credits)

*(27 July 2014: This is a new work-in-progress; many changes are expected.)*

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

Create virtual environment

    user:~/flask-base 
    $ virtualenv venv

Activate virtual environment

    user:~/flask-base 
    $ python venv/bin/activate

pip install required packages (edit requirements as necessary)

    (venv) $ pip install -r requirements/dev.txt

Create database

    (venv) $ python manage.py shell
    >>> from app import db
    >>> db.create_all()

***

####Credits

Structure and scripts pulled from various sources, including: 

* https://github.com/miguelgrinberg/flasky
* http://maximebf.com/blog/2012/11/getting-bigger-with-flask/
* http://pythonthusiast.pythonblogs.com/230_pythonthusiast/archive/1369_flask_biography_tutorial_part_xiv-redesign_the_application_using_blueprints.html

