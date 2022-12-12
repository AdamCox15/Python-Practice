favorite_word = "Ovechkin"
print(favorite_word)

my_name = "Adam"
first_initial = my_name[0]
print(first_initial)

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)

print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)
print(temp_password)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2:-1]
final_word = company_motto[-4:]
print(final_word)

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]

password = "theycallme\"crazy\"91"

name = "Adam"
def get_length(str):
  return len(str)

print(get_length(name))
