def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))

# -----------------------------------

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
  
print(append_sum([1, 1, 2]))

# -----------------------------------

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# -----------------------------------

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# -----------------------------------

def combine_sort(lst1, lst2):
  unsorted_lst = lst1 + lst2
  sorted_lst = sorted(unsorted_lst)
  return sorted_lst

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# -----------------------------------

