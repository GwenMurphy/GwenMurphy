import time

day = 12
month = 'May'
temp = 69
crush1 = 'Karen Gillan'
crush2 = 'Ella Balinska'
ta = 'L\'Agence Townsend'

a = 0

while a < 5:
    time.sleep(1)
    if a == 1:
        print('Today is October 21st and it\'s 65 degrees Fahrenheit outside.')
    elif a == 2:
        print(f'Today is October {day} and it\'s {temp} degrees Fahrenheit outside')
    elif a == 3:
        print(f'Today is {month} {day} and it\'s {temp} degrees Fahrenheit outside.')
    elif a == 4:
        print(f'Welcome to {ta} and today, I\'m being sandwiched between the loves of my life, {crush1} and {crush2}.')
    print(a)
    a += 1
    