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

# Size or length
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]

# Opposite using not
booleans = [True, False, True]
opposite = [not bool for bool in booleans]

# Same string 
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]

# Greater than two
nums = [5, -10, 40, 20, 0]
greater_than_two = [num > 2 for num in nums]

# Product ---- new list, multiple items from sub lists
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [item1 * item2 for (item1, item2) in nested_lists]
print(product)

# Greater than
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [item1 > item2 for (item1, item2) in nested_lists]

# First Only prints only the first item in a sub-list
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [item[0] for item in nested_lists]

# Add with a zip
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [item1 + item2 for (item1, item2) in zip(a, b)]

# Divide with zip
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [item1 / item2 for (item2, item1) in zip(a,b)]


