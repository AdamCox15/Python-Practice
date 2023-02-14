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

