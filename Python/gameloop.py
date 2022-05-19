guess = int(input('What is your guess?: '))
correct_number = 69
guesses = 1

while guess != correct_number:                    #Combination of if and for loops.
    guesses += 1
    guess = int(input('What is your guess?: '))
    

if guesses == '1':
    print(f'You got the right answer in {guesses} guess. It was {correct_number}.')    
elif guesses != '1':
    print(f'You got the right answer in {guesses} guesses. It was {correct_number}.')
