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

