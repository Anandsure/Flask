# Flask
A interactive, blog. Hosted on FLASK web server
# Tech Stack:
1) Python, Flask module, Flask-Sqlalchemy extension
2) HTML, CSS, BOOTSTRAP FRAMEWORK
# Front End:
  1) Front end is entirely, HTML codes with CSS and BOOTSTRAP as the framework.
  2) The About, Home, Login, Registration and LAYOUT pages were created as seperate templates,
  and are present in the templates folder under Flasktest.
  3) The 'main.css', referenced in the 'layout.html' template is present in the static folder
  and is the same css pattern followed by all the routes.
  4) 'layout.html' contains all the common HTML code for Home and About pages.
  5) the concept of '{% codeblocks %}' is used to integrate the templates with the 'layout.html'
# Back End:
  1) The routes are present in the 'routes.py' file programmed with Flask module in Python v3.7. 
  2) The Login and Registration forms draw imports from 'forms.py' which contain a built in model FlaskForm.
  the FlaskForm extension does all the form 'Validation', minimising code end.
  3) 'forms.py' contains 2 classes which are imported into their respecive templates using the codeblocks.
  4) '__init.py' contains the Creation of the database 'site.db' and initialisation of the 'db' variable
  which is later imported in 'models.py'.
  5) The creation of the database is done with the SQLAlchemy extension of flask.
  6) 'models.py' is the module which creates and maintins users and posts. The system incorporated here is called
  "multi to one". In DB terms, 1 'user' (author) can have many 'posts' but 1 'post' can have only 1 'author'.
  7) Hence the 'User' class is linked to the 'Post' class usind 'db.relationship('Post',backref='author', lazy=True)'
  command.
  8) 'site.db' is the database file available locally on the host PC directories.
# Requirements: 
  To run the blog on your base system, install the following modules using your CLI: </br>
  1) $ pip install flask
  2) $ pip install datetime
  3) $ pip install flask-wtf
  4) $ pip install flask-sqlalchemy
  5) $ pip install wtforms </br>
  </br>
If the above CLI install's don't work, Try </br?
  $ pip install --upgrade pip </br>
  or </br> $ curl https://bootstrap.pypa.io/get-pip.py | python3 </br>
  Prefferably, use Python3.7 since Python is stopping services for v2.7
  
  
