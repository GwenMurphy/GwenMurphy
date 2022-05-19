import time

day = 21
weight = 190.4
month = 'October'
are_printers_annoying = False

light_is_on = False
a = -25

while a < 1000:
    print(a)
    if a == 0:
        are_printers_annoying = True
        print('All printers are annoying, especially the RICOH MP 3554.')
    if a == 10:
        light_is_on = True
    if a == 20:
        light_is_on = False
    if light_is_on:
        print('The light is on!')
    a += 1
    time.sleep(0.5)
    
# Find something around you that could be represented by a Boolean and make a variable for items

