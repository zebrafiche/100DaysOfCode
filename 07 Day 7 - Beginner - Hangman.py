# 066 Day 7 Goals_ what we will make by the end of the day

# By the end pf the day we will be creating a hangman game.

# We will use concepts like

# if/else
# list
# strings
# range
# modules





# 067 How to break a Complex Problem down into a Flow Chart

# Draw a flow diagram of the problem and how you want the program to progress with varying inputs




# 068 Challenge 1 - Picking a Random Words and Checking Answers

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


import random
chosen_word = random.choice(word_list)

guess = input('Choose a letter - ').lower()

for l in chosen_word:
    if l == guess:
        print('Right')
    else:
        print('Wrong')



# 069 Challenge 1 Solution - How to Check the User's Answer





# 070 Challenge 2 - Replacing Blanks with Guesses

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

# TODO 1
display = []
s = ''
for i in range(0, len(chosen_word)):
    display.append('_')
    s = s + " " + "_"
print(display)
print(s)

# alternative

# for letter in chosen_word:
#     display = display + "_"
#     s = s + " " + "_"
# print(display)
# print(s)

# TODO 2

guess = input('Choose a letter - ').lower()


for l in range (len(chosen_word)):
    if chosen_word[l] == guess:
        display[l] = guess
# TODO 3
        print(display)






# 071 Challenge 2 Solution - How to Replace the Blanks





# 072 Challenge 3 - Checking if the Player has Won

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

# TODO 1
display = []
s = ''
for i in range(0, len(chosen_word)):
    display.append('_')
    s = s + " " + "_"
print(display)

while '_' in display:

    guess = input('Choose a letter - ').lower()


    for l in range (len(chosen_word)):
        if chosen_word[l] == guess:
            display[l] = guess
    # TODO 3
            print(display)


if '_' not in display:
    print("You've won")




# 073 Challenge 3 Solution - How to Check if the Player Won





# 074 Challenge 4 - Keeping Track of the Player's Lives

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6
import random
chosen_word = random.choice(word_list)

display = []
s = ''
for i in range(0, len(chosen_word)):
    display.append('_')
    s = s + " " + "_"
print(' '.join(display))

end_of_game = False
while not end_of_game:

    guess = input('Choose a letter - ').lower()


    for l in range (len(chosen_word)):
        if chosen_word[l] == guess:
            display[l] = guess
    
    print(' '.join(display))

    if guess not in chosen_word:
        lives -= 1  

    if lives == 0:
        end_of_game = True
        print('You lose')
    
    print(stages[lives])

    if '_' not in display:
        end_of_game = True
        print("You've won")






# 076 Challenge 5 - Improving the User Experience

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-2: - Import the stages from hangman_art.py and make this error go away.
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.



import hangman_words
import hangman_art

print(hangman_art.logo)
lives = 6
import random
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
guesses = []

display = []
s = ''
for i in range(0, len(chosen_word)):
    display.append('_')
    s = s + " " + "_"
print(' '.join(display))

end_of_game = False
while not end_of_game:

    guess = input('Choose a letter - ').lower()


    if guess in guesses:
        print("You've already guessed this one")
    else:
        guesses += guess

        for l in range (len(chosen_word)):
            if chosen_word[l] == guess:
                display[l] = guess
        
        print(' '.join(display))

        if guess not in chosen_word:
            print(f"You've guessed {guess}. It is not in the word.")
            lives -= 1  

        if lives == 0:
            end_of_game = True
            print('You lose')
        
        print(hangman_art.stages[lives])

        if '_' not in display:
            end_of_game = True
            print("You've won")





# 077 Challenge 5 Solution - How to Add ASCII Art and Improve the UI





# 078 The Benefits of Daily Practice