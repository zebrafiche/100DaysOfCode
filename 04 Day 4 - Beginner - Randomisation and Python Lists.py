# 039 Day 4 Goals_ what we will make by the end of the day

# Randomization is really useful, because if we want to create something different each time, maybe a game, then there has to be sth random
# We will be creating a rock paper scissors game by the end of the day




# 040 Random Module 

#  Computers are basically deterministic, meaning they are pre programmed to geberate what we want
# How cna we then generate sth random out of computers?
# There is a whole lot of maths that goes behind creating randomness for computers
# The one pythons uses is called the Marsenne Twister

# Watch a video from Khan Academy called Pesudorandom Number Generatos
# Another useful website - Askpython.com

import random
rand_int = random.randint(1, 10)
print(rand_int)
# 3

# What is a module?
# Scripts responsible for a specific purpose

# How can we write out own modules?
# We can create another python file that generates a specific response and import that file as a module here

# So I have created another python file, that only has the variable pi set to 3.14 and named it samplemodule 
import samplemodule
print(samplemodule.pi)
# 3.14
# So that is how you create your own modules

# That is how tha random module works as well, it is just another script 


# Create a random float 

rand_float = random.random()
# from askpython.com - 
# random.random() -> Returns the next random floating point number between [0.0 to 1.0)
# random.uniform(a, b) -> Returns a random floating point N such that a <= N <= b if a <= b and b <= N <= a if b < a.
print(rand_float)

# 0.6268100312348868
# 0.3670361263802595

# generates random number everytime, between 0.0 and 1.0 (not including 1.0 btw)

# One way to generate random float between two ranges is to multiply the random.random() with sth 
# random.random() gives us floats between 0.0 and 1.0 right?
# so multipying random.random() with 5 should essentially give random floats between 0.0 and 5.0 right?




# 041 [Interactive Coding Exercise] Heads or Tails

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 
# **Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, 
# either 0 or 1. Then use that number to print out Heads or Tails.

import random

output = random.randint(1,2)
if output == 1:
    print('Heads')
else:
    print('Tails')



# 042 Understanding the Offset and Appending Items to Lists 

# A list is what you would call a data structure - a way of organizing and storing data in python 
# fruits = [item1, item2]
# The order is also important - 
almamater = ['Maple Leaf', 'North South', 'IBA']
print(almamater[0])
print(almamater[1])
# Maple Leaf
# North South

print(almamater[-1])
print(almamater[-2])
print(almamater[-3])
print(almamater[-4])
# IBA
# North South
# Maple Leaf
# IndexError: list index out of range

# timestamp = 08:59 


# Change items in the list 

almamater = ['Maple Leaf', 'North South', 'IBA']
almamater[0] = 'Dhanmondi Intl'
print(almamater)
# ['Dhanmondi Intl', 'North South', 'IBA'] 


# Adding to a list 

almamater.append('Maple Leaf')
print(almamater)
# ['Dhanmondi Intl', 'North South', 'IBA', 'Maple Leaf']

# Other functions -
# Adding multiple items to the end of the list 

almamater.extend(['Blizzard', 'BBC'])
print(almamater)
# ['Dhanmondi Intl', 'North South', 'IBA', 'Maple Leaf', 'Blizzard', 'BBC'] 




# 043 [Interactive Coding Exercise] Banker Roulette - Who will pay the bill_

# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill. 

# **Important**: You are not allowed to use the `choice()` function.

# **Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. 
# For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name.

# Example Input
# ```
# Angela, Ben, Jenny, Michael, Chloe
# ```
# Note: notice that there is a space between the comma and the next name. 

# # Example Output

# ```
# Michael is going to buy the meal today!


# str.split() separates a string into a list, delimiting on the parameter (space, comma) passed as the argument

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(', ')
print(names)
# ['Rafi', 'Numayer', 'Mahedi', 'Arif']

import random
print(names[random.randint(0, len(names)-1)])
# Because last item happens at index 3, so 0 to 3
# Mahedi

# Alternative with choice() function -
import random
names = ['Rafi', 'Numayer', 'Mahedi', 'Arif']
roulette = random.choice(names)
print(roulette)
# Arif

# random.choice() picks a random item from a list 





# 044 IndexErrors and Working with Nested Lists

# IndexError: list index out of range occurs when the index specified does not exist in the list

# Nested Lists
# Lists within a list 


schools = ['Dhanmondi Intl.', 'Maple Leaf', 'Study Town', 'Qudrat Sirs', 'Shaan Sirs']
varsities = ['North South', 'IBA']

education = [schools, varsities]
print(education)

# [['Dhanmondi Intl.', 'Maple Leaf', 'Study Town', 'Qudrat Sirs', 'Shaan Sirs'], ['North South', 'IBA']]




# 045 [Interactive Coding Exercise] Treasure Map 

# You are going to write a program which will mark a spot with an X.
# In the starting code, you will find a variable called ```map```.

# This ```map``` contains a nested list.
# When ```map``` is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ```
# In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
# ```
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ```
# This is to try and simulate the coordinates on a real map. 

# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit for the input will specify the column (the position on the horizontal axis). The second digit in the input will specify the row number (the position on the vertical axis). 
# First your program must take the user input and convert it to a usable format. 
# Next, you need to use it to update your nested list with an "x". 

# # Example Input 1
# column 2, row 3 would be entered as:
# 23

# # Example Output 1
# ```
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', 'X', '⬜️']


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

list_num = int(position) % 10
item_num = int(position) // 10
# can also do this with string indexing

map[list_num -1][item_num - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")






# 046 Day 4 Project_ Rock Paper Scissors

# Make a rock, paper, scissors game. 

# Start the game by asking the player:

# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out: 
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player. 


game_count = 0
win_count = 0
while True:
    user_res = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    options = ['Rock', 'Paper', 'Scissors']
    import random
    comp_res = random.randint(0, 2)

    colu_user_inp = ["Rock","Pap","Scis"]
    row1_comp_roc = ["Draw","Win","Lose"]
    row2_comp_pap = ["Lose","Draw","Win"]
    row3_comp_sci = ["Win","Lose","Draw"]
    map = [row1_comp_roc, row2_comp_pap, row3_comp_sci]
    # print(f"{row1}\n{row2}\n{row3}")

    outcome = map[comp_res][user_res]
    print(f'You chose {options[user_res]}, and the computer chose {options[comp_res]}. You {outcome}')
    game_count += 1
    print(game_count)
    if outcome == 'Win':
        win_count += 1
    repeat = input('Play Again? (Y/N)')
    if repeat == 'Y':
        continue
    else:
        break
print(f'You played {game_count} times. You won {win_count} times')
