from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''<h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new friend</P>
  <ul><a href="/animals/dogs"><li>Dogs</li></a><a href ="/animals/cats"><li>Cats</li></a><a href ="/animals/rabbits"><li>Rabbits</li></a></ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  return f'<h1>List of {pet_type}</h1>'
