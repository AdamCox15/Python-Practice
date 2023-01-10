print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []

# --------------------------------

class Facade:
  pass

facade_1 = Facade

facade_1_type = type(facade_1)
print(facade_1_type)

#  ------------------------------

class Grade:
  minimum_passing = 65
