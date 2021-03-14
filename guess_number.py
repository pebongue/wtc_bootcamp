import random
'''
A random integer number will be created between 0 and 10

Then, the program will ask the user to guess for that number.

"Correct" is display if the user is right, else "Wrong answer"
'''

#using a loop for multiple guesses. The user can stop the program by typing 'X'
while True:
    rnd_guess = random.randint(0,10)
    guess_number = input("Guess an integer between 0 and 10 [To stop, input=X]:")

    if guess_number == 'X':
        break

    if int(guess_number) == rnd_guess:
        print("Correct")
        continue
    else:
        print("Wrong answer. \n The right number was {}".format(rnd_guess))

print("All done! Thanks for playing.")
