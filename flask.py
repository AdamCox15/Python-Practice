# Importing the Flask class from the flask module

from flask import Flask

app = Flask(__name__)

print(__name__)

# Routing with render HTML

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'


@app.route('/reporter')
def reporter():
      return '''
    <h2>Reporter Bio</h2>
    <a href="/">Return to home page</a>
    '''

#   Routing with variable rules "Dynamic URLS"

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return '''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''
#  Adding a third view function

@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.replace('-', ' ').title()}</h2>
  <a href='/'>Return back to home page</a>
  '''
 
    
#  ---------- Intro to Authentication ----------
#  Flask-Login 

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, Authentication World!'

# Protecting Pages by importing login_required and using the @login_required decorator

import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from flask import request, render_template, flash, redirect,url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = flask.Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password) 

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
    
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
@login_required
def home():
	return render_template('logged_in.html')






