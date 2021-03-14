#Simple 'hello world' - as old as programming lol
print("Hello World")

import random



guesses = 0



print('Hello! What is your name?')

name = input()



number = random.randint(1,20)

print(name, 'I am thinking of a number  between 1 and 20.')



while guesses <6:

    print('Take a guess.')

    guess = input()

    guess = int(guess)



    guesses = guesses + 1



    if guess < number:

        print('Your guess is too low.')



    if guess > number:

        print('Your guess is too high.')



    if guess == number:

        

        number = str(number)

        print('Good job', name, '! You guessed my number in', guesses ,'guesses!')

