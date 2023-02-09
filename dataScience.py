# ----- Data Science in Python --------

import numpy as np
import statsmodels as sm
import seaborn as sns

# ---- Creating a float -----

bayes_age = 4.0
print(bayes_age)

#  ---- Creating strings -----

favorite_toy = "Mr. Squeaky"
owner = 'DataCamp'

#  --- Correcting string errors -----

birthday = "2017-07-14'
case_id = 'DATACAMP!123-456?
# fixed below 
birthday = '2017-07-14'
case_id = 'DATACAMP!123-456?'

#  ---- Loading the DataFrame ------

import pandas as pd

r = pd.read_csv('ransom.csv')

print(r)
