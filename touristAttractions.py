# ---------- App.py -----------------

from flask import Flask, render_template, request, redirect, url_for
from locations import Locations

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_PROJECT'

visit = Locations()
categories = {"recommended": "Recommended", "tovisit": "Places To Go", "visited": "Visited!!!", }

UP_ACTION = "\u2197"
DEL_ACTION = "X"

@app.route("/<category>", methods=["GET", "POST"])
def locations(category):
  locations = visit.get_list_by_category(category)
  ## Check the request for form data and process
  if False:
    [(name, action)] = [(None, None)]

    if action == UP_ACTION:
      visit.moveup(name)
    elif action == DEL_ACTION:
      visit.delete(name)
      
    return render_template("locations.html", category=category, categories=categories, locations=locations)

@app.route("/add_location", methods=["POST"])
def add_location():
  ## Validate and collect the form data

  if True:
      name=None
      description=None
      category=None
      visit.add(name, description, category)

  ## Redirect to locations route function
  return ""

@app.route("/")
def index():

  ## Redirect to locations route function
  return ""

# ------------------ locations.html ----------------

<!-- extend from "base.html" here -->

<!-- begin block content here -->

  <h1>{{ categories[category] }}</h1>

  <div class="navbar">
   {% for category, label in categories.items()%}
      <a href="{{ category }}">{{ label }}</a>
    {% endfor %}

  </div>

  <table>
    <colgroup>
      <col style="width: 20%">
      <col style="width: 70%">
      <col style="width: 10%">
    </colgroup>
    <tbody class="loctable">
        {% for location in locations %}

        <tr>
          <td class="loc">{{ location.name }}</td> 
          <td class="desc">{{ location.description }}</td> 
          <td class="btns">
            <!-- start if statement here -->

            <form method="POST">
              <input type="submit" class="up" name="{{ location.name }}" value=&#8599;>
              <input type="submit" class="del" name="{{ location.name }}" value="X"> 
            </form>
            <!-- end if statement here -->

          </td>
        </tr>
        {% endfor %}

    </tbody>
  </table>

  <form class="addform" action="" method="POST"> <!-- set action attribute here -->
    <!-- call hidden_tag() here -->

    <table>
      <colgroup>
        <col style="width: 40%">
        <col style="width: 40%">
        <col style="width: 20%">
      </colgroup>
      <tbody>
        <tr>
          <td></td> <!-- insert location name label here -->
          <td></td> <!-- insert location description label here -->
          <td></td> <!-- insert location category label here -->
        </tr>
        <tr>
          <td></td> <!-- insert add_location name here -->
          <td></td> <!-- insert add_location description here -->
          <td>
            <!-- begin for loop here -->

              <div></div> <!-- insert button here -->
            <!-- end for loop here -->

          </td>
        </tr>
        <tr>
          <td></td> <!-- insert submit here -->
        </tr>
      </tbody>
    </table>
  </form>
<!-- end block content here -->

# ------------------ forms.py ----------------- 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class FieldsRequiredForm(FlaskForm):
  """Require radio fields to have content. This works around the bug that WTForms radio fields don't honor the `DataRequired` or `InputRequired` validators."""
  class Meta:
    def render_field(self, field, render_kw):
      if field.type == "_Option":
        render_kw.setdefault("required", True)
      return super().render_field(field, render_kw)

categories = [("recommended","Recommended"), ("tovisit", "Places To Go"), ("visited", "Visited!!!")]
