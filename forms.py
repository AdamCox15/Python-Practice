# ------------ Flask forms practice --------------
# ------- Get/Post requests and request forms/ FlaskForm Class ------------
# --------- app.py ----------------

from flask import Flask, render_template, request, redirect, url_for
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import RecipeForm, CommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route("/", methods=["GET", "POST"])
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
    new_id = len(recipes)+1
    recipes[new_id] = recipe_form.recipe.data
    types[new_id] = recipe_form.recipe_type.data
    descriptions[new_id] = recipe_form.description.data
    new_ingredients = recipe_form.ingredients.data
    new_instructions = recipe_form.instructions.data
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
    comments[new_id] = 
        return redirect(url_for("recipe", id=new_id, _external=True, _scheme='https'))
  return render_template("index.html", template_recipes=recipes, template_form=recipe_form)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  # Instantiated form class 
  comment_form = CommentForm(csrf_enabled=False)
  # appended data from comment form to comments list  
  if True:
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], template_form=comment_form)

@app.route("/about")
def about():
  return render_template("about.html")

#  ------ forms.py ------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
  recipe_categories = [("Breakfast","Breakfast"), ("Lunch","Lunch"), ("Dinner","Dinner")]
  recipe = StringField("Recipe", validators=[DataRequired()])  
  #### Add `recipe_type` and assign it a new radio field instance
  recipe_type = RadioField("Type", choices=recipe_categories)
  description = StringField("Description")
  ingredients = TextAreaField("Ingredients")
  instructions = TextAreaField("Instructions")
  submit = SubmitField("Add Recipe")

class CommentForm(FlaskForm):
  comment = StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Add Comment")

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



