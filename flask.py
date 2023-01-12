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
  
  
