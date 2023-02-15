#  ------- List Comprehension practice ----------------

nums = [4, 8, 15, 16, 23, 42]
double_nums = [num * 2 for num in nums]

# Squared nums
nums = range(11)
squares = [num**2 for num in nums]

# Adding ten
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]

# Divide by two
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num / 2 for num in nums]

# Parity ----- Even or odd
nums = [4, 8, 15, 16, 23, 42]
parity = [num % 2 for num in nums]

# Concatenate strings ---- adding hello
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]

# First character ---- index
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]

