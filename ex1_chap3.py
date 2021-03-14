import random

"""
This program should allow the user to guess a number between a certain range
To simplify the problem we will only be using integers only
"""
#range values - you can change the values before running the program
lower_range = 10
upper_range = 200

#receive an store the number I am thinking about
rnd_number = random.randint(lower_range, upper_range)

print(f"I am thinking of a number between {lower_range} and {upper_range}.")

#set user initial guess to dummy value and count guesses to zero
user_guessing_number = -1
count_guesses = 0

#use a while loop to get the user to guess the number
while user_guessing_number != rnd_number:
    user_guessing_number = int(input("Take a guess.\n"))

    #if the guessed number is not in the required range, ask again
    if (user_guessing_number < lower_range) or (user_guessing_number > upper_range):
        print("Your number needs to be in the range {} and {}".format(lower_range, upper_range))
        continue

    #increase the guesses after each one - a guess is a valid number in range
    count_guesses += 1

    #determine the distance between user's number and mine
    number_distance = rnd_number - user_guessing_number

    if number_distance == 0:
        print(f"Good job! You guessed my number in {count_guesses} guesses!")
    elif number_distance > 0:
        print("Your guess is too low.")
    else:
        print("Your number is too high.")