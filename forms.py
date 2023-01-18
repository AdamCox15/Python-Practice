# ------------ Flask forms practice --------------
# ------- Get/Post requests and request forms/ FlaskForm Class ------------
# --------- app.py ----------------

from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

# Created form class 
class CommentForm(FlaskForm):
  comment = StringField("Comment")
  submit = SubmitField("Add Comment")

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  # Instantiated form class 
  comment_form = CommentForm()
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], template_form=comment_form)

@app.route("/about")
def about():
  return render_template("about.html")

# ------------ Route Selection -------------------

# ------------ Updated base.html -------

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

# ------------ Updated index.html --------------

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

# -------------- Updated recipe.html ---------------

{% extends "base.html" %}
{% block content %}
  <h1>{{ template_recipe | title }}</h1>
  {% if template_description %}
    <p>{{ template_description }}</p>
  {%else%}
    <p>A {{ template_recipe }} recipe.</p>
  {% endif %}
  <h3>Ingredients - {{ template_ingredients | length}}</h3>
  <ul>
  {% for ingredient in template_ingredients %}
      <li>{{ ingredient }}</li>
  {% endfor %}
  </ul>
  <h3>Instructions</h3>
  <ul>
  {% for key, instruction in template_instructions|dictsort %}
      <li>{{ instruction }}</li>
  {% endfor %}
  </ul>
  <h3>Comments</h3>
  <ul>
  {% for comment in template_comments %}
    <li>{{ comment }}</li>
  {% endfor %}
  </ul>
  <form method="POST">
  <!-- Inserted StringField  -->  
  {{ template_form.hidden_tag() }}
  {{ template_form.comment.label }}
  {{ template_form.comment() }}
  {{ template_form.submit()}}    
  </form>
{% endblock %}



