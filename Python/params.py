import random

def WinVista(name):
    print(f'Prynhawn da, {name}! I have some news for you: Windows Vista is shite.')
    
WinVista("Gwen")

def addnums(num1, num2):
    print(num1 * num2)
    
addnums(2, -50000000)
for x in range(100):
    addnums(random.randint(1,10000000000),random.randint(-1000000000000000, 1000000000000000))