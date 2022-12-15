# Module Practice

from datetime import datetime

current_time = datetime.now()
print(current_time)

# --------------------------------

import random

random_list = [random.randint(1,100) for i in range(101)]

randomer_number = random.choice(random_list)

print(randomer_number)

# --------------------------------

import codecademylib3_seaborn

from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()

# --------------------------------

from decimal import Decimal

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# --------------------------------
def always_three():
  return 3
# ------Below i'm showing how to import always_three from a seperate file -------
from library import always_three

print(always_three())

# --------------------------------



# --------------------------------




# --------------------------------
