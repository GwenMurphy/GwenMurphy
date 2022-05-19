# Picking random numbers. What could possibly go wrong?

import random
import time

print(random.randint(69, 420))
# Generates random integer between 69 and 420. Prints it too.

print(random.random())

# Make your own version of a magic 8 ball that prints yes, no, or maybe each time you ask it.

answer = random.rantint(1,3)

if answer == 1:
    print('Yes')
elif answer == 2:
    print('No')
elif answer == 3:
    print('Maybe')