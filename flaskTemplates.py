from flask import Flask
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <h1>Cooking By Myself</h1>
        <p>Welcome to my cookbook. These are recipes I like.</p>
        <a href="/recipe/1">Fried Egg</a>
      </body>
    </html>
    '''

@app.route("/recipe/<int:id>")
def recipe(id):
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <a href="/">Back To Recipe List</a>
        <p>names[id] = ''' + recipes[id] + '''</p>
        <p>descriptions[id] = ''' + descriptions[id] + '''</p>
        <p>ingredients[id] = ''' + str(ingredients[id]) + '''</p>
        <p>instructions[id] = ''' + str(instructions[id]) + '''</p>
      </body>
    </html>
    '''
# -----------Changing to render templates BELOW-----

from flask import Flask, render_template
from helper import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  
  #### Returning a rendered index.html file
  return render_template("index.html")

@app.route("/recipe/<int:id>")
def recipe(id):
    
  #### Returning a rendered fried_egg.html file
  return render_template("fried_egg.html")

# ----------- new render templated html file below ----------

<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe }}</h1>
    <p>{{ template_description }}</p>
    <h3>Ingredients</h3>
    <ul>
      <!-- Ingredients list elements
      should fill the <li> tags -->
      <li>{{template_ingredients[0]}}</li>
      <li>{{template_ingredients[1]}}</li>
      <li>{{template_ingredients[2]}}</li>
    </ul>
  </body>
</html>

# ----------- Updated py file below ---------------

from flask import Flask, render_template
from helper import recipes, descriptions, ingredients

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/recipe/<int:id>")
def recipe(id):
  #### Added template variables as 
  #### variable assignment arguments
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id])

