# 089 Day 9 Goals_ what we will make by the end of the day

# By the end of the day we will build a silent auction program, kinda like ebay
# We will need to learn
# Python dictionaries



# 090 The Python Dictionary_ Deep Dive

# Every dictionary has two parts to it, key and value 
# {Key: Value}
# {'Bug':'An error in a program'}

# You add more pairs to a dictionary by adding the comma


# By convention, when programmers work with dictionaries, they start off with the curly brace and continue the dict in the next line.
# In the next line, each pair is written separately and indented.
# When done, the closing curly brace is added without the indent

# And another thing that's quite nice to do is to cap off all entries in your
# dictionary or list with a comma.
# This means that if you needed to add more items into the dictionary
# you can simply just hit enter and continue typing the next thing.

# And if we wanted to add another entry,
# it's a simple as adding in the key, a colon and then the value and to cap it
# off again with a comma.


# Let's work with a sample dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# Getting items from a dictionary 
print(programming_dictionary["Bug"])
# An error in a program that prevents the program from running as expected.

# If we had written the keys without the quotation marks python would have considered them variables 
# and since no variable named bug was defined it would have thrown an error.

# We can also use integers as keys, in those cases we do not need quotation marks to call on a key 


# Adding new items after the dictionary has been created
programming_dictionary["Loop"] =  "The action of doing something over and over again"
print(programming_dictionary)
# {'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again'}

# It might be helpful to start out with an empty programming_dictionary like this
empty_dict = {}


# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
# {}


# Edit an item in the dictionary 
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
# {'Bug': 'A moth in your computer', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again'}


# Looping through a dictionary 
for thing in programming_dictionary:
    print(thing)
# Bug
# Function
# Loop

for thing in programming_dictionary:
    print(programming_dictionary[thing])
# A moth in your computer
# A piece of code that you can easily call over and over again.
# The action of doing something over and over again



# 091 [Interactive Coding Exercise] Grading Program

# You have access to a database of `student_scores` in the format of a dictionary. 
# The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**. 

# This is the scoring criteria:
# > Scores 91 - 100: Grade = "Outstanding"
# > Scores 81 - 90: Grade = "Exceeds Expectations"
# > Scores 71 - 80: Grade = "Acceptable"
# > Scores 70 or lower: Grade = "Fail"

# Write a program that **converts their scores to grades**. 
# By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values**. 
# **The final version** of the `student_grades` dictionary will be checked.

# **DO NOT** write any print statements.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 80 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 70 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# {
#     'Harry': 'Exceeds Expectations', 
#     'Ron': 'Acceptable', 
#     'Hermione': 'Outstanding', 
#     'Draco': 'Acceptable', 'Neville': 'Fail'
# }




# 092 Nesting Lists and Dictionaries

# Dictionaries can also be like this - 
# {
#     Key1: [List]
#     Key2: {Dict}

# }

# examples - 

# Dictionary of capitals of countries
capitals = {
    "France": "Paris"
    "Germany": "Berlin"
}

# Dictionary for all the cities I have been to for each country
travel_log = {
    "France" : ['Paris', 'Lille', 'Dijon']
    "Germany" = ["Berlin", "Hamburg", "Stuttgart"]
    'Netherlands' = ['Hague', 'Amsterdam']
}


# Nesting is not limited to dictionaries
# There are nested lists, i.e. list within a list

# Dictionary nested within a dictionary 
travel_log = {
    "France" : {"cities_visited" : ['Paris', 'Lille', 'Dijon'], "total_visits" : 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 13},
    'Netherlands' : {"cities_visited" : ['Hague', 'Amsterdam'], "total_visits" : 0}
}


# Nesting a dictionary inside a list 
# Unlike lists, items inside a dictionary are accessed using the key 

travel_log = [
    {
    "country" : "France",  
    "cities_visited" : ['Paris', 'Lille', 'Dijon'], 
    "total_visits" : 12
    }
    {
    "country" : "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits" : 13
    }
    {
    "country" : 'Netherlands', 
    "cities_visited" : ['Hague', 'Amsterdam'], 
    "total_visits" : 0
    }
]
# Here I have converted the mother dictionary into a list, so now I can access items using indexing





# 093 [Interactive Coding Exercise] Dictionary in List

# You are going to write a program that adds to a `travel_log`. 
# You can see a travel_log which is a **List** that contains 2 **Dictionaries**. 
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the `travel_log`. 

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# > `You've visited Russia 2 times.`
# > `You've been to Moscow and Saint Petersburg.`

# **DO NOT** modify the `travel_log` directly. You need to create a function that modifies it. 


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities_list):
    new_dict = {"country": country, "visits": visits, "cities": cities_list}
    travel_log.append(new_dict)
    



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)





# 094 The Secret Auction Program Instructions and Flow Chart 

# The objective is to write a program that will collect the names and bids of different people. 
# The program should ask for each bidder's name and their bid individually. 

# Welcome to the secret auction program. 
# What is your name?: Angela
# ```
# ```
# What's your bid?: $123
# ```
# ```
# Are there any other bidders? Type 'yes' or 'no'.
# yes

# ```
# If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid. 

# ```
# The winner is Elon with a bid of $55000000000
# ```

# Use your knowledge of Python dictionaries and loops to solve this challenge. 


import os
def clear():
    os.system('cls') 
    # "clear" for mac/linux, "cls" for windows 
from secretauctionart import logo
print(logo)
bid = {}
gamecontinue = True
while gamecontinue == True:
    value = input('What is your name?: ')
    key = int(input("What's your bid?: $"))
    bid[key] = value
    if input("Are there any other bidders? Type 'yes' or 'no'. - ") == 'no':
        gamecontinue = False
    else:
        clear()
winningbid = 0
for i in bid:
    if i > winningbid:
        winningbid = i
print(f"The winner is {bid[i]} with a bid of {winningbid}")





# 095 Solution and Complete Code for the Secret Auction Program

# Alternative solution to find the highest bidder

import os
def clear():
    os.system('cls')
from secretauctionart import logo
print(logo)
bid = {}
gamecontinue = True
while gamecontinue == True:
    key = input('What is your name?: ')
    value = int(input("What's your bid?: $"))
    bid[key] = value
    if input("Are there any other bidders? Type 'yes' or 'no'. - ") == 'no':
        gamecontinue = False
    else:
        clear()
winningbid = 0
winner = ""
for i in bid:
    if bid[i] > winningbid:
        winningbid = bid[i]
        winner = i
print(f"The winner is {winner} with a bid of {winningbid}")


# Note - The os.system('cls') does not work in IDLE, but does in vscode




# 096 Motivation and the Accountability Trick