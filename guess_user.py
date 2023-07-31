import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H) or too low (L) or correct (C) ').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print("computer guessed number")
comp_guess(10)