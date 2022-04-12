import random
secretnumber=random.randint(1,20)
print('Im thinking of a number between 1 to 20')

for guessestaken in range(1,7):
    print('Take a guess')
    guess=int(input())

    if guess < secretnumber:
        print('Your guess is too low')

    elif guess > secretnumber:
        print('Your guess is too high')

    else:
        break

if guess == secretnumber:
    print('Great job! You guessed my number in ' + str(guessestaken) + ' guess!')
else:
    print('Incorrect Guess! The number I was thinking of was' + str(secretnumber))
