# ----- Data Science in Python --------

import pandas as pd
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

#  ----- Correcting a function error -----

plt.plot(x_values y_values)

plt.show()
# Fixed
plt.plot(x_values, y_values)

plt.show()

#  ---- Creating a variable for a license plate number ------

plate = 'FRQ****'

lookup_plate(plate)
lookup_plate(plate, color='Green')

#  ------- Loading a DataFrame -------
# Always us alias as pd for pandas
import pandas as pd 

credit_records = pd.read_csv('credit_records.csv')

print(credit_records.head())

#  ----- Inspecting DataFrame ------

print(credit_records.info())

#  ------ Two methods for selecting columns --------

items = credit_records['item']
items = credit_records.item

# ------- More column selecion mistakes fixed -------

print(mpr.info())
name = mpr.['Dog Name']
is_missing = mpr['Missing?']

#  ------ Logical Testing --------

print(height_inches > 70)
print(plate1 == "FRQ123")
print(fur_color != "brown")

#  ------- Selecting missing puppies -------

greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)

#  ------ Narrowing the list of suspects --------

purchase = credit_records[credit_records.location == 'Pet Paradise']

print(purchase)










