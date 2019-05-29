import random

secretNumber = random.randint(1,5)
print('The secret number is ' + str(secretNumber))
guess = -1
numberOfGuesses = 0

while guess != secretNumber:
    numberOfGuesses += 1
    
    guess = input('\nPlease guess a number between 1 and 5\n')
    try:
        guess = int(guess)
    except:
        print('You must enter a number')
    print('You guessed a ' + str(guess))

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        print('You got it!')

print('\nIt took you ' + str(numberOfGuesses) + ' tries.')