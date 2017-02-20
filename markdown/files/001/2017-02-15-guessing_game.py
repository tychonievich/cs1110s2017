import random # if you make a file named random.py, this line will cause problems

answer = random.randrange(1, 10001)

name = input('Who are you? ')
if name == 'admin':
    print('I am thinking of the number', answer)
else:
    print('Welcome,', name, 'to this guessing game!')
guess = float(input('Guess a number between 1 and 10000: '))

if guess == answer:
    print('You guessed it!')
else:
    print('No, I was thinking of', answer, 'not', guess)