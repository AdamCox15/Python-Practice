# ------------ Flask forms practice --------------
# ------- Get/Post requests and request forms ------------

from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  new_id = len(recipes) + 1
  if len(request.form) > 0:
    recipes[new_id] = request.form["recipe"]
    descriptions[new_id] = request.form["description"]
    new_ingredients = request.form["ingredients"]
    new_instructions = request.form["instructions"]
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>")
def recipe(id):
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id])

@app.route("/about")
def about():
  return render_template("about.html")

# ------------ Route Selection -------------------

# ------------ Updated Base HTML -------

<!DOCTYPE html>
<html>
  <body>
    <div>
      <a href="{{ url_for('index') }}">Recipes</a>
      <a href="{{ url_for('about') }}">About</a>
    </div>
    {% block content %}
    {% endblock %}
  </body>
</html>

# ------------ Updated Index HTML --------------

{% extends "base.html" %}
{% block content %}
  <h1>Cooking By Myself</h1>
  <p>Welcome to my cookbook. These are recipes I like.</p>
  {% for id, name in template_recipes.items() %}
    <p><a href="{{ url_for('recipe', id=id) }}">{{ name }}</a></p>
  {% endfor %}

  <form action="/" method="POST">
    <h3>Add Recipe</h3>
    <p>
      <label for="recipe">Name:</label>
      <input type="text" name="recipe"/>
    </p>
    <p>
      <label for="description">Description:</label>
      <textarea name="description"></textarea>
    </p>
    <p>
      <label for="ingredients">Ingredients:</label>
      <textarea name="ingredients"></textarea>
    </p>
    <p>
      <label for="instructions">Instructions:</label>
      <textarea name="instructions"></textarea>
    </p>
    <p><input type="submit" name="submit_recipe"/></p>
  </form>
{% endblock %}





