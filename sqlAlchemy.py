# Practice with Flask SQLAlchemy
#  ------ Importing ------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#database configuration
app = Flask(__name__) #application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app) #database instance


#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just created your first Flask application supporting databases!"

# ------------- Declaring a model: Book ------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warnings
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    title = db.Column(db.String(80), index = True, unique = True) # book title
    #Checkpoint #1: insert your code here
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of book suggestion
    author_name = db.Column(db.String(50), index = True, unique = False)
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)

@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just made your first Flask-SQLAlchemy model declaration!"

#  ------- Declaring a model: Reader ---------

class Reader(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), index = True, unique = False)
  surname = db.Column(db.String(80), index = True, unique = False)
  email = db.Column(db.String(120), index = True, unique = True)
  
  def __repr__(self):
      return "Reader: {}".format(self.email)

#  ------ Part 1: Declaring relationships One-to-many -------------

class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(80), unique = False, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    #added relationship column here
    reviews = db.relationship('Review', backref = 'reviewer', lazy = 'dynamic')
  
  
    def __repr__(self):
        return "Reader: {}".format(self.email)
    
#  ----- Part:2 Declaring relationships (Foregin Keys) -----------

    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    
#  ------- Putting it all together: initializing the database --------

$ python3

>>> from app import db

>>> db.create_all()

#  ---- Creating database entries: entities -----------

from app import Reader, Book, Review

b1 = Book(id = 123, title = 'Demian', author_name = "Hermann", author_surname = 'Hesse', month = "February", year = 2020)
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')

print("My first reader:", r1.name)

b2 = Book(id= 533, title = 'The Stranger', author_name = 'Albert', author_surname = 'Camus', month = 'April', year = 2019)
#Checkpoint 2: 
r2 = Reader(id = 765, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')

print(b2.author_surname)

print(len(r2.email))

#  ----------- Creating database entries: relationships ------------

rev2 = Review(id = 450, text = 'This book is difficult!', stars = 2, reviewer_id = r2.id, book_id = b2.id)

print(len(rev2.text.split()))

#  ---- Queries: query.all() and query.get() ------

from app import db, Book, Reader, Review, Annotation

readers = Reader.query.all()
print(readers)

reader = Reader.query.get(123)
print(reader)

reader = Reader.query.get(450)
print("Reader with id = ", reader.id, "is called", reader.name)

for reader in readers:
  print(reader.email)

reviews = Review.query.all()
for review in reviews:
  print(review.text)

for review in reviews:
  print(review.text)

book_1 = Book.query.get(12)

# ------- Databases in Flask - Reading, Updating and Deleting -------

from app import db, Book, Reader, Review, Annotation

#Fetching 'many' objects
reader = Reader.query.get(123) #fetch a reader with id = 123
reviews_123 = reader.reviews.all() #fetch all reviews made by reader wiith id = 123
[print(review.id) for review in reviews_123]
#check the image on the right - Ann Adams (id = 123, wrote reviews with ids 111 and 113)

#fetching 'one' object
review = Review.query.get(111) #fetch a review with id = 111
reviewer_111 = review.reviewer #get the reviewer for review with id = 111. There's only one!
print("The author of [", review, "] is", reviewer_111)

#By chaining we avoid using temporary variables
reviews_123 = Reader.query.get(123).reviews.all() #same result as line 5
reviewer_111 = Review.query.get(111).reviewer #same result as line 10

print("\nCheckpoint 1: fetch all the reviews made for a book with id = 13.")
book_13 = Book.query.get(13).reviews.all()
[print(book.id) for book in book_13]

print("\nCheckpoint 2: fetch all the annotations made for a book with id = 19.")
book_19_an = Book.query.get(19).annotations.all()
[print(annotation.id) for annotation in book_19_an]

print("\nCheckpoint 3: fetch the reader who owns the annotation with `id = 331.`")
author_331 = Annotation.query.get(331).author
print(author_331)

#  ------- Databases in Flask - Reading, Updating and Deleting "filtering" -------

from app import Book, Reader, Review, Annotation

#selected books from the year 2020
book_2020 = Book.query.filter(Book.year == 2020).all()
print("All the suggested books in the year 2020:")
[print(book) for book in book_2020]

book_2020_first = Book.query.filter(Book.year == 2020).first()
print("\nThe first book fetched from the year 2020: ", book_2020_first)

#specify multiple criteria for filtering
rev_3_boook13 = Review.query.filter(Review.stars <= 3, Review.book_id == 13).all()
print("\nThe review of 3 stars or lower written for a book with id = 13: ", rev_3_boook13)

#fetching all the readers with "Adams" surname
adams = Reader.query.filter(Reader.surname == 'Adams').all()
[print(person) for person in adams]

#fetching the first book dating prior to the year 2019
book_pre2019 = Book.query.filter(Book.year <= 2019).first()
print(book_pre2019)

#  ---------- More advanced filtering -----------------

from app import db, Book, Reader, Review

#retrieved all reader with .edu e-mails
education = Reader.query.filter(Reader.email.endswith('edu')).all()
print(education)

#retrieved all readers with e-mails that contain a . before the @ symbol
emails = Reader.query.filter(Reader.email.like('%.%@%')).all()
print("\nReaders with e-mails having a . before the @ symbol:")
for e in emails:
  print(e.email)

#ordered all books by year below
ordered_books = Book.query.order_by(Book.year).all()
print("\nBooks ordered by year:")
for book in ordered_books:
  print(book.title, book.year)

print("\nCheckpoint 1: your code here below:")
s_names = Reader.query.filter(Reader.surname.endswith('s')).all()
print(s_names)

print("\nCheckpoint 2: your code here below:")
sample_emails = Reader.query.filter(Reader.email.like('%@sample%')).all()
print(sample_emails)

print("\nCheckpoint 3: your code here below:")
ordered_reviews = Review.query.order_by(Review.stars).all()
print(ordered_reviews)

#  ----------- Session: add and rollback -----------

new_reader = Reader(name = "Peter", surname = "Johnson", email = "peter.johnson@example.com") 

db.session.add(new_reader)

try: 
  db.session.commit()
except:
  db.session.rollback()

#  ------------- Session: updating existing entires --------

book_19 = Book.query.get(19)
book_19.month = 'June' 
db.session.commit()

#  ----- Session: Removing database entries "cascading deletion" ---------

#  in app.py changed the relationship() by adding a cascade parameter
reviews = db.relationship('Review', backref='reviewer', lazy='dynamic', cascade = 'all, delete, delete-orphan')

db.session.delete(Reader.query.get(123))

#  ----- Queries and templates --------

@app.route('/reviews/<int:review_id>')
def reviews(review_id):
   review = Review.query.filter_by(id = review_id).first_or_404(description = "There is no user with this ID.")
   return render_template('review.html', review = review)

#  ------- more practice stuff to reference later ------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_library.db'

class Song(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  artist = db.Column(db.String(120), index = True, unique = False)
  title = db.Column(db.String(120), index = True, unique = False)
  n = db.Column(db.Integer, index = False, unique = False)
  def __reper__(self):
    return f"{self.title} by {self.author}"

class Item(db.Model):
  id = db.Column(db.Integer, primary_key = True) 
  song_id = db.Column(db.Integer, db.ForeignKey('song.id') )
    
class Playlist(db.model):
  id = db.Column(db.Integer, primary_key = True)
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
  items = db.relationship('Item', backref = 'playlist', lazy = 'dynamic')

# --------- Intro to Hashing ----------

from werkzeug.security import generate_password_hash, check_password_hash

hardcoded_password_string = "123456789_bad_password"

hashed_password = generate_password_hash(hardcoded_password_string)
print(hashed_password)

password_attempt_one = "abcdefghij_123456789"

hash_match_one = check_password_hash(hashed_password, password_attempt_one)
print(hash_match_one)

password_attempt_two = "123456789_bad_password"

hash_match_two = check_password_hash(hashed_password, password_attempt_two)
print(hash_match_two)

#  -------- Modeling accounts with SQLAlchemy --------

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index = True, unique = True)
  password_hash = db.Column(db.String(128))
  joined_at = db.Column(db.DateTime(), index = True, default = datetime.utcnow)

#  --------- Signing up with WTForms ----------

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  # add email field here:
  email = StringField('Email', validators = [DataRequired(), Email()]
  # add password fields here:
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators= [DataRequired(), EqualTo('password')])
  
  submit = SubmitField('Register')

                                           
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User(username = form.username.data, email = form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)

#  ----- Login with Flask ---------------
                      
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

# instantiate application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), unique = True, index = True)
  password_hash = db.Column(db.String(128))
  joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

# registration form
class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

# login form
class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')

# registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)

# user loader
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# login route
@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    # query User here:
    user = User.query.filter_by(email=form.email.data).first()
    # check if a user was found and the form password matches here:
    if user and user.check_password(form.password.data):
      # login user here:
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='https'))
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)

# user route
@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('user.html', user=user)

# landing page route
@app.route('/')
def index():
  # grab all guests and display them
  current_users = User.query.all()
  return render_template('landing_page.html', current_users = current_users)

# --------------- Associating User Actions --------
                      
@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.filter_by(party_host_id=user.id)
  if dinner_parties is None:
    dinner_parties = []
  form = DinnerPartyForm(csrf_enabled=False)
  if form.validate_on_submit():
    # update the values of each attribute to the corresponding form data here:
    new_dinner_party = DinnerParty(
      date = form.date.data,
      venue = form.venue.data,
      main_dish = form.main_dish.data,
      number_seats = int(form.number_seats.data), 
      party_host_id = user.id,
      attendees = username)
    db.session.add(new_dinner_party)
    db.session.commit()
  return render_template('user.html', user=user, dinner_parties=dinner_parties, form=form)

# rsvp route
@app.route('/user/<username>/rsvp/', methods=['GET', 'POST'])
@login_required
def rsvp(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.all()
  if dinner_parties is None:
    dinner_parties = []
  form = RsvpForm(csrf_enabled=False)
  if form.validate_on_submit():
    # query the DinnerParty model here:
    dinner_party = DinnerParty.query.filter_by(id=int(form.party_id.data)).first()
    # updated the attendees here:
    dinner_party.attendees += f", {username}"
    db.session.commit()
  return render_template('rsvp.html', user=user, dinner_parties=dinner_parties, form=form)

# landing page route
@app.route('/')
def index():
  # grabed all guests and display them
  current_users = User.query.all()
  return render_template('landing_page.html', current_users = current_users)

# ------- Success and Error Handling -------------
                      
@app.route('/user/<username>/rsvp/', methods=['GET', 'POST'])
@login_required
def rsvp(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.all()
  if dinner_parties is None:
    dinner_parties = []
  form = RsvpForm(csrf_enabled=False)
  if form.validate_on_submit():
    dinner_party = DinnerParty.query.filter_by(id=int(form.party_id.data)).first()
    # try block
    try:
      dinner_party.attendees += f", {username}"
      db.session.commit()
      # query to find the host of dinner_party
      host = User.query.filter_by(id=int(dinner_party.party_host_id)).first()
      # add RSVP success message here:
      flash(f"You successfully RSVP'd to {host.username}'s dinner party on {dinner_party.date}!")
    # except block
    except:
      # add the RSVP failure message here
      flash("Please enter a valid Party ID to RSVP!")
  return render_template('rsvp.html', user=user, dinner_parties=dinner_parties, form=form)
