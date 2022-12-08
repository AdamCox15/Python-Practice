def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))

# ------------------------------------

def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False
 
print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))

# ------------------------------------

def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False
  
print(always_false(0))
print(always_false(-1))
print(always_false(1))

# ------------------------------------

def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"

print(movie_review(9))
print(movie_review(4))
print(movie_review(6))

# ------------------------------------
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
  
print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))




