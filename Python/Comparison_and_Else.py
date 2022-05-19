import time


light_is_on = True
x = 0
weight = 190
a = 0


while a < 500:
    print('Weight is', weight, 'and x is', x, 'and a is', a)
    a = weight + x
    time.sleep(0.1)
    x += 1
    weight -= 1
    if x == weight:
        print('Ry\'n ni yma o hyd, er gwaetha pawb a phopeth.')
    elif a == x:
        print('Hodgkinson\'s Law -- What can go wrong will go wrong, especially if printers are involved.')
        x -= 1
    if weight + x != 190:
        print('STOP')
        a += 10000
