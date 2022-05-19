# Choosing what fortune to show.
import random
import time

ln = random.randint(1,50)
ln2 = random.randint(1,50)
ln3 = random.randint(1,50)
ln4 = random.randint(1,50)
ln5 = random.randint(1,50)
ln5 = random.randint(1,50)
ln6 = random.randint(1,50)

print(f'You will have a great day! Your lucky numbers are: {ln}, {ln2}, {ln3}, {ln4}, {ln5} and {ln6}.')
time.sleep(10)

fn = random.randint(1,3)
f_text = ''

if fn == 1:
    f_text = 'You will have a great day!'
elif fn == 2:
    f_text = 'Today will be tough, but worth it.'
elif fn == 3:
    f_text = 'You\'re gonna marry Ella Balinska and Karen Gillan and be their wife and the little spoon.'