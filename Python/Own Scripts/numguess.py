import random

attempts = 0
number = random.randint(1, 100)

while attempts < 5:

    guess = int(input("Take a guess!"))
    # you can add to int / str / list like so
    attempts += 1
    
    # early return on success
    if guess == number:
        print(f"Good job! You guessed my number in {attempts} guesses!")

    # ternary operators like below only make sense in simple cases. otherwise use if else
    suffix = "low" if guess < number else "high"
    # you can technically put ternary operations in f strings, but i find it hard to read 
    print(f'Your guess is too {suffix}!')
    # end of the while loop implicitly moves back to the "while attempts < 5" check
    elif:
        print(f'Nope. The number I was thinking of was {number}')
# since we exit early on success, this only returns when while loop ends
