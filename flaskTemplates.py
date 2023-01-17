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

# ----------- new render templated recipe html file below ----------

<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe | title  }}</h1>
    <p>{{ template_description | default("A" + template_recipe + "recipe")}}</p>
    <h3>Ingredients - {{template_ingredients | length}}</h3>
    <ul>
      <!-- Ingredients list elements
      should fill the <li> tags -->
      <li>{{template_ingredients[0]}}</li>
      <li>{{template_ingredients[1]}}</li>
      <li>{{template_ingredients[2]}}</li>
    </ul>
     <h3>Instructions</h3>
    <ol>
      <li>{{ template_instructions | dictsort }}</li>
    </ol>
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
  return render_template("recipe.html", template_recipe=recipes[id], template_ingredients=ingredients[id], template_instructions=instructions[id])

# -------------- Adding if statements to the recipe html template -------

<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe | title }}</h1>
   
    {% if template_description %}
    <p>{{ template_description }}</p>
    
    {% else %}
    <p>A {{ template_recipe }} recipe.</p>
    
    {% endif %}
    <h3>Ingredients - {{ template_ingredients | length}}</h3>
    <ul>
      <li>{{ template_ingredients[0] }}</li>
      <li>{{ template_ingredients[1] }}</li>
   
      {% if template_ingredients | length == 3 %}
      <li>{{ template_ingredients[2] }}</li>
      
      {% endif %}
    </ul>
    <h3>Instructions</h3>
    <ol>
      <li>{{ template_instructions | dictsort }}</li>
    </ol>
  </body>
</html>

# ---------- index html ------------------

<!DOCTYPE html>
<html>
  <body>
    <h1>Cooking By Myself</h1>
    <p>Welcome to my cookbook. These are recipes I like.</p>
    <!-- Implement a for loop using `template_recipes`-->
    {% for id, name in template_recipes.items() %}
    <p><a href="/recipe/{{ id }}">{{ name }}</a></p>
  {% endfor%}
  </body>
</html>

#  --------------- recipes html updated ----------------

<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe | title }}</h1>
    {% if template_description %}
      <p>{{ template_description }}</p>
    {%else%}
      <p>A {{ template_recipe }} recipe.</p>
    {% endif %}
    <h3>Ingredients - {{ template_ingredients | length}}</h3>
    <ul>
      <!-- Implement a for loop to iterate through 
      `template_ingredients`-->
      {% for ingredient in template_ingredients %}
      <li>{{ ingredient }}</li> 
      {% endfor %}
    </ul>
    <h3>Instructions</h3>
    <ul>
    {% for key, instruction in template_instructions|dictsort %}
      <p>{{ key }}: {{ instruction }}</p>
    {% endfor %}
    </ul>
  </body>
</html>
