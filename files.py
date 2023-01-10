with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)
    
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

#  ------------ Using the write method ----------
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("Jonas Brothers")
  
  
# -------- Using the append method ------------
ith open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")
  
with open("fun_file.txt") as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

  print(setup)
  
 with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())
 
# ----------- Rading csv as a Dictionary -----------
import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])
