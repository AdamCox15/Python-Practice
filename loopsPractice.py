def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# ---------------------------------

def add_greetings(names):
  lst = []
  for name in names:
    lst.append("Hello, " + name)
  return lst

print(add_greetings(["Owen", "Max", "Sophie"]))

# ---------------------------------

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# ---------------------------------

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

# ---------------------------------

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))

# ---------------------------------

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

# ---------------------------------

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# ---------------------------------

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

print(max_num([50, -10, 0, 75, 20]))

# ---------------------------------

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# ---------------------------------

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))

print(reversed_list([1, 5, 3], [3, 2, 1]))
