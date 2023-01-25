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
  ## Return the main template with variables
  return ""

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

  <h1></h1> <!-- insert category here -->

  <div class="navbar">
    <!-- begin for loop here -->

      <a href=""></a> <!-- set attribute and text here -->
    <!-- end for loop here -->

  </div>

  <table>
    <colgroup>
      <col style="width: 20%">
      <col style="width: 70%">
      <col style="width: 10%">
    </colgroup>
    <tbody class="loctable">
        <!-- begin for loop here -->

        <tr>
          <td class="loc"></td> <!-- insert location name here -->
          <td class="desc"></td> <!-- insert location description here -->
          <td class="btns">
            <!-- start if statement here -->

            <form method="POST">
              <input type="submit" class="up" name="" value=&#8599;> <!-- set name attribute here -->
              <input type="submit" class="del" name="" value="X"> <!-- set name attribute here -->
            </form>
            <!-- end if statement here -->

          </td>
        </tr>
        <!-- end for loop here -->

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
