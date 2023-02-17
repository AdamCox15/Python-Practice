# ----- Data Science in Python --------

import pandas as pd
import numpy as np
import statsmodels as sm
import seaborn as sns

#  ------ Example of matplotlib import and using it, also showing multiple lines ---------

from matplotlib import pyplot as plt

plt.plot(data1.x_values, data1.y_values)
plt.plot(data2.x_values, data2.y_values)

plt.show()

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

# -------- matplotlib import and checking officers hours worked --------

from matplotlib import pyplot as plt

plt.plot(deshaun.day_of_week, deshaun.hours_worked)
plt.plot(aditya.day_of_week, aditya.hours_worked)
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

plt.show()

#  ------- Adding a Legend ------

plt.plot(deshaun.day_of_week, deshaun.hours_worked, label = 'Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

plt.legend()
plt.show()

#  -------- Adding labels -------

plt.title('Hours worked chart')
plt.ylabel('Hours')

#  ------ Adding floating text -----

plt.plot(six_months.month, six_months.hours_worked)
plt.text(2.5, 80, 'Missing June data')

plt.show()

#  ------- Color and linestyle -------

# Phoenix color changed to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=":")

# Square markers for Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker="s")

plt.legend()
plt.show()

#  ----- Playing with styles ---------
# style fivethirtyeight
plt.style.use('fivethirtyeight')
# style ggplot
plt.style.use('ggplot')
# style dark_background
plt.style.use('dark_background')

# View all styles use this in the console
print(plt.style.availabe)

plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

#  ------ Plotting letter frequencies from ransom note ---------

plt.plot(ransom.letter, ransom.frequency, label="Ransom", linestyle=':', color='gray')

plt.show()

#  ------- Plotting a line for the data in suspect1 and suspect2 ---------

plt.plot(suspect1.letter, suspect1.frequency, label="Fred Frequentist")

plt.plot(suspect2.letter, suspect2.frequency, label="Gertrude Cox")

plt.show()

#  ------ Labeling x, y axis and adding legend --------

plt.xlabel("Letter")
plt.ylabel("Frequency")

plt.legend()

#  --------- Charting data using scatter plots --------

print(cellphone.head())

plt.scatter(cellphone.x, cellphone.y)

plt.ylabel('Latitude')
plt.xlabel('Longitude')

plt.show()

#  -------- Modifying the scatterplot  changing color, marker and alpha-----------

plt.scatter(cellphone.x, cellphone.y, color='red', marker='s', alpha=0.1)

#  ------- Building a simple bar chart --------------

plt.bar(hours.officer, hours.avg_hours_worked)
        
plt.show()

# Adding a yerr 'error bar' 
plt.bar(hours.officer, hours.avg_hours_worked,yerr=hours.std_hours_worked)
# Addded label
plt.bar(hours.officer, hours.desk_work, label="Desk Work")
# Added bottom
plt.bar(hours.officer, hours.field_work, bottom= hours.desk_work, label='Field Work')

plt.legend()
plt.shop()

# ----------- Modifying histograms/histogram practice ---------------

plt.hist(puppies.weight, bins=50, range=(5, 35))

plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

plt.show()

plt.hist(gravel.radius, bins=40, range=(2, 8), density=True)

plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# --------------- Inspecting a dataframe --------------------

# .head() returns the first few rows (the “head” of the DataFrame).
print(homelessness.head())
# .info() shows information on each of the columns, such as the data type and number of missing values.
print(homelessness.info())
# .shape returns the number of rows and columns of the DataFrame.
print(homelessness.shape)
# .describe() calculates a few summary statistics for each column.
print(homelessness.describe())

# ------- Parts of a DataFrame ----------------

# .values: A two-dimensional NumPy array of values.
print(homelessness.values)
# .columns: An index of columns: the column names.
print(homelessness.columns)
# .index: An index for the rows: either row numbers or row names.
print(homelessness.index)

# --------- Sorting rows ------------------------

homelessness_ind = homelessness.sort_values("individuals")
print(homelessness_ind.head())

homelessness_fam = homelessness.sort_values("family_members", ascending = False)
print(homelessness_fam.head())

homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])
print(homelessness_reg_fam.head())

#  ---------- Subsetting columns ------------

individuals = homelessness["individuals"]
print(individuals.head())

state_fam = homelessness[["state", "family_members"]]
print(state_fam.head())

ind_state = homelessness[["individuals", "state"]]
print(ind_state.head())

