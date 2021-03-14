import random

#this is the hangman game 
#the user gets a random word with a missing letter and has to guess it

#ask the user for his or her name
player_name = input("Input your name :")
print(f"Hi {player_name}! Lets play hangman ...")

#get the random word
words_list = ['semantic', 'synonym', 'between', 'python', 'antonyms', 'relationship', 'available', 'dictionary', 'friendly', 'bourgeois', 'stunning', 'admirable', 'perserverance']
rnd_word = random.choice(words_list)

#record or pick a random character from the random selected word
rnd_char_index = random.randint(0, len(rnd_word))

#keep record of the right character being guessed
rnd_char_guessed = rnd_word[rnd_char_index]

#replace the selected random character with the undercore
word_missing_char = rnd_word.replace(rnd_char_guessed, '_')

#guess missing letter
guess_missing_letter = input(f"Guess the missing letter in '{word_missing_char}' :")

#give feedback or display answer
if guess_missing_letter == rnd_char_guessed:
    print("Good guess!")
else:
    print("Incorrect.")

#display the random word
print("The word was: {}".format(rnd_word))