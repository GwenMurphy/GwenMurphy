# This program says hello and asks for my name.
print('Hello, world!')
print()
print('What is your name?') #Ask for their name.
myName = input()
print()
print('It is good to meet you, ' + myName)
print()
print('The length of your name is:')
print(len(myName))
print()
print('What is your age?')  #Ask for their age.
myAge = input()
print()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
