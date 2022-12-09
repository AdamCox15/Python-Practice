def tenth_power(num):
  return num ** 10

print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))

# ------------------------

def square_root(num):
  return num ** 0.5
  
print(square_root(16))
print(square_root(100))

# ------------------------

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100

print(win_percentage(5, 5))
print(win_percentage(10, 0))

# ------------------------

def average(num1, num2):
  return (num1 + num2) / 2

print(average(1, 100))
print(average(1, -1))

# ------------------------

def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

print(remainder(15, 14))
print(remainder(9, 6))

# ------------------------
