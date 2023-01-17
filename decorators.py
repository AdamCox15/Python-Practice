# 1. Functions are objects

def add_five(num):
  print(num + 5)
  
add_five(2)

# 2. Functions within functions

def add_five(num):
  def add_two(num:
      return num +2
              
  num_plus_two = add_two(num)
  print(num_plus_two + 3)

# add_two(7) can't use function outside of add_five           
              
add_five(10)

# 3. Returning functions from functions
 
def get_math_function(operation): # + or - 
    def add(num1, num2):
        return num1 + num2
    def sub(num1 - num2):
        return num1 - num2
    
    if operation == '+':
       return add
    elif operation == '-':
         return sub
              
add_function = get_math_funtion('+')
sub_function = get_math_function('-')

# 4. Decorating a function
              
def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper
              
def print_my_name():
    print("Adam")

def print_rooks_name():
    print("Rook")
              
              
decorated_function = title_decorator(print_rooks_name) 
              
decorated_function()
              
# 5. Decorators
              
def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper
              
@title_decorator               
def print_my_name():
    print("Adam")
              
@title_decorator
def print_rooks_name():
    print("Rook")
        
print_my_name()
print_rooks_name()             
              
#  6. Decorators with Parameters
              
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        print_name_function(*args, **kwargs)
    return wrapper
              
@title_decorator               
def print_my_name(name, age):
    print(name + " your are" + str(age))
                    
print_my_name("Dekker")
