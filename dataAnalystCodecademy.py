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
