# ----------- Notes on Data Analyst codecademy program -------------

SELECT * FROM page_visits

# --------- importing pandas ----------

import codecademylib
import pandas as pd


# Load data
df = pd.read_csv('page_visits.csv')

# Display data
print(df.head())

# Display survey results
print(
  df.groupby('website_goal')\
  	.first_name.count()\
  	.reset_index()\
  	.rename(columns={'first_name': 'number_of_citizens'}))

#  -------- visualize the data with matplotlib --------

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

# Loading data
df = pd.read_csv('page_visits.csv')

# Calculating survey results
survey_results = df.groupby('website_goal')\
  	.first_name.count()
  
# Making a pie chart
plt.pie(survey_results.values,
        labels=survey_results.index,
        autopct='%d%%'
       )
plt.title('Why do citizens visit our website?')
plt.axis('equal')

plt.show()

# ------- Hypothesis Testing for A/B Tests "testing for significance" -------

from scipy.stats import chi2_contingency

control_group = 7700
variant_group = 7700
control_success = 231
variant_success = 308
control_fail = control_group - control_success
variant_fail = variant_group - variant_success

results = chi2_contingency([
  [control_fail, control_success],
  [variant_fail, variant_success]
])

p = results[1]

if p < 0.05:
    print("Significant!")
if p > 0.05:
    print("Not significant!")
