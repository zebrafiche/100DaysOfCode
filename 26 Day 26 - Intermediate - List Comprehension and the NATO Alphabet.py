# 232 Day 26 Goals_ what you will make by the end of the day

# Today we are going to learn about list and dictionary comprehensions
# This is something that is rally unique to the python

# Cuts down a lot of code writing

# By the end of the day we will have built a project to use the NATO phonetic alphabet
# So we can use spell out various things on the telephone

# We will enter a word, and the program will return a list of words, each starting with each letter of the word


# 233 How to Create Lists using List Comprehension

# List comprehension is really unique to the python language
# It significantly cuts down on the amount of typing

# What exactly is list comprehension?
# It is a case where you create a new list from a previous list

# For example -
# What if I have a list -
sample_list = [1, 2, 3]
# and I wanted to create a new list where each number would be incremented by 1
# I would use the for loops
new_list = []
for i in sample_list:
    i = i + 1
    new_list.append(i)
print(new_list)
# [2, 3, 4]

# Now, under the list comprehension principle it would look something like this-
# new_list = [new_item for item in list]
# OR, new_list = [do_this for item in list]

# So according to the formula above, replace new_item/do_this, item and list -
new_list = [i + 1 for i in sample_list]
# Let's do i+10 for better comprehension
new_list = [i + 10 for i in sample_list]
print(new_list)

# [11, 12, 13]

name = 'Angela'
new_list = [l for l in name]
print(new_list)
# ['A', 'n', 'g', 'e', 'l', 'a']

# In python, lists, ranges, strings and tuples are called sequences
# Which means they have a specific order
# When you preform a list comprehension, it performs an operation to the sequence under that order
# So we can do list comprehension with them as well
new_list = [i*2 for i in range(1, 5)]
print(new_list)
# [2, 4, 6, 8]

# Conditional List Comprehension
# same as list comprehension, but we add a condition
# new_list = [new_item/do_this for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# In PyCharm, if you want to change the spelling of "Elanor", you can do so directly from the console]
# Execute it, the list will be available in the console
# Expand names > Elanor > (right click) set value > Eleanor
print(names)
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Create a new list of names made up of the short names, i.e. names made up of four letters or less

new_names = [i for i in names if len(i) <= 4]
print(new_names)
# ['Alex', 'Beth', 'Dave']

# Challenge - create a new list from names, but each name should be uppercase

new_names = [i.upper() for i in names]
print(new_names)
# ['ALEX', 'BETH', 'CAROLINE', 'DAVE', 'ELEANOR', 'FREDDIE']
new_names = [i.upper() for i in names if len(i) <= 4]
print(new_names)
# ['ALEX', 'BETH', 'DAVE']


# 234 [Interactive Coding Exercise] Squaring Numbers

# You are going to write a List Comprehension to create a new list called `squared_numbers`.
# This new list should contain every number in the list `numbers` but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [n**2 for n in numbers]

# Write your code 👆 above:

print(squared_numbers)
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]


# 235 [Interactive Coding Exercise] Filtering Even Numbers

# You are going to write a List Comprehension to create a new list called `result`.
# This new list should only contain the even numbers from the list `numbers`.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

# Write your code 👆 above:

print(result)
# [2, 8, 34]


# 236 [Interactive Coding Exercise] Data Overlap

# Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

file1 = []
with open('file1.txt') as file:
    for i in file.readlines():
        file1.append(int(i))
print(file1)
# [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
file2 = []
with open('file2.txt') as file:
    for i in file.readlines():
        file2.append(int(i))
print(file2)
# [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

result = [n for n in file2 if n in file1]

# Write your code above 👆

print(result)
# [3, 6, 13, 5, 7, 12, 3, 33, 42]
# if we do [n for n in file1 if n in file2], then -
# [3, 6, 5, 33, 12, 7, 42, 13]


# 237 Apply List Comprehension to the U.S. States Game

# In our US states game, before a part of the code was like this -

if formatted_answer == 'Exit':
    for i in states_list:
        if i not in correct_answers_list:
            undiscovered_states.append(i)
    # undiscovered_states = {
    #     'states_not_guessed': undiscovered_states
    # }
    # no need to create the dict, just feed the list to pandas, that will also do
    us_df = pandas.DataFrame(undiscovered_states)
    us_df.to_csv('undiscovered_states.csv')
    break

# Change it using the List Comprehension method -

if formatted_answer == 'Exit':
    undiscovered_states = [i for i in states_list if i not in correct_answers_list]
    # for i in states_list:
    #     if i not in correct_answers_list:
    #         undiscovered_states.append(i)
    # undiscovered_states = {
    #     'states_not_guessed': undiscovered_states
    # }
    # no need to create the dict, just feed the list to pandas, that will also do
    us_df = pandas.DataFrame(undiscovered_states)
    us_df.to_csv('undiscovered_states.csv')
    break

# check by changing the code in the game file
# Works


# 238 How to use Dictionary Comprehension

# The formula is
# new_dict = {new_key: new_value for item in list/range/tuple if test}

# Dictionary comprehension is just a way of creating a new dictionary using shortened syntax

# Another formula is
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# A reminder -

sample_dict = {
    "rafi": "teetly",
    "sakib": "nafia",
    "zawad": "femina",
    "asif": "kanta"
}
for i in sample_dict.items():
    print(i)
# ('rafi', 'teetly')
# ('sakib', 'nafia')
# ('zawad', 'femina')
# ('asif', 'kanta')

for (key, value) in sample_dict.items():
    print(key, value)
# rafi teetly
# sakib nafia
# zawad femina
# asif kanta

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# create a new dictionary where each name is a key and each value is a random score given to that name
# new_dict = {new_key: new_value for item in list/range/tuple if test}
import random
student_scores = {
    item: random.randint(70, 100) for item in names
}
print(student_scores)
# {'Alex': 86, 'Beth': 79, 'Caroline': 90, 'Dave': 87, 'Elanor': 75, 'Freddie': 73}
# You can see that a new student dictionary has been created in the console

# Loping through a dictionary
# Use the student_scores dict
# create a new dict that loops through student_scores & keeps those who scored more than 80, since 80 is pass mark

new_dict = {
    key: value for (key, value) in student_scores.items() if value > 80
}
print(new_dict)
# {'Alex': 86, 'Caroline': 90, 'Dave': 87}


# 239 [Interactive Coding Exercise] Dictionary Comprehension 1

# You are going to use Dictionary Comprehension to create a dictionary called `result`
# that takes each word in the given sentence and calculates the number of letters in each word.
#
# Try Googling to find out how to convert a sentence into a list of words.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

sentence_list = sentence.split()
print(sentence_list)
# ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']

result = {item: len(item) for item in sentence_list}

print(result)

# {
#     'What': 4,
#     'is': 2, 'the': 3,
#     'Airspeed': 8,
#     'Velocity': 8,
#     'of': 2,
#     'an': 2,
#     'Unladen': 7,
#     'Swallow?': 8
# }


# 240 [Interactive Coding Exercise] Dictionary Comprehension 2

# You are going to use Dictionary Comprehension to create a dictionary called `weather_f` that takes each
# temperature in degrees Celsius and converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f:
# ```
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}

print(weather_f)
#
# {
#     'Monday': 53.6,
#     'Tuesday': 57.2,
#     'Wednesday': 59.0,
#     'Thursday': 57.2,
#     'Friday': 69.8,
#     'Saturday': 71.6,
#     'Sunday': 75.2
# }


# 241 How to Iterate over a Pandas DataFrame

# Looping through a dictionary

student_dict = {
    "students" : ['Amy', 'James', 'Angela'],
    "scores" : [76, 36, 65]
}

for (k, v) in student_dict.items():
    print(k)
    print(v)

# students
# ['Amy', 'James', 'Angela']
# scores
# [76, 36, 65]

# You can loop through a dataframe the same way you loop through a dictionary

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

#   students  scores
# 0      Amy      76
# 1    James      36
# 2   Angela      65

print(student_df['students'])
# 0       Amy
# 1     James
# 2    Angela
# Name: students, dtype: object

for (k, v) in student_df.items():
    print(k)
    print(v)

# students
# 0       Amy
# 1     James
# 2    Angela
# Name: students, dtype: object
# scores
# 0    76
# 1    36
# 2    65
# Name: scores, dtype: int64

# this is not particularly useful, because it is a hassle to isolate a single value (e.g. score) from this
# to mitigate this, pandas has an inbuilt method called iterrows for looping

for i in student_df.iterrows():
    print(i)

# (0, students    Amy
# scores       76
# Name: 0, dtype: object)
# (1, students    James
# scores         36
# Name: 1, dtype: object)
# (2, students    Angela
# scores          65
# Name: 2, dtype: object)

for (k,v) in student_df.iterrows():
    # Iterate over DataFrame rows as (index, Series) pairs.
    # k = The index of the row.
    # v = The data of the row as a Series.
    print(v)

# students    Amy
# scores       76
# Name: 0, dtype: object
# students    James
# scores         36
# Name: 1, dtype: object
# students    Angela
# scores          65
# Name: 2, dtype: object
#
# each row has a student value and a score value

for (k,v) in student_df.iterrows():
    print(k)

# 0
# 1
# 2

for (index,rows) in student_df.iterrows():
    print(rows['students'])
    print(rows.scores)

# Amy
# 76
# James
# 36
# Angela
# 65

# You can do the indexing by [] or by '.'

for (index,rows) in student_df.iterrows():
    if rows.students == 'Amy':
        print(rows.scores)

# 76


# 242 Introducing the NATO Alphabet Project

# Todos
# 1. Import csv using pandas and convert it to dataframe
# 2. Convert dataframe to dictionary, identify why this will not work
# 3. Create a dictionary using the NATO phonetic alphabet format
# 4. Create a list of the phonetic code words from the words that the user inputs


# 1. Import csv using pandas and convert it to dataframe

import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(data)

#   letter      code
# 0       A      Alfa
# 1       B     Bravo
# 2       C   Charlie
# 3       D     Delta
# 4       E      Echo
# 5       F   Foxtrot
# 6       G      Golf
# 7       H     Hotel
# 8       I     India
# 9       J    Juliet
# 10      K      Kilo
# 11      L      Lima
# 12      M      Mike
# 13      N  November
# 14      O     Oscar
# 15      P      Papa
# 16      Q    Quebec
# 17      R     Romeo
# 18      S    Sierra
# 19      T     Tango
# 20      U   Uniform
# 21      V    Victor
# 22      W   Whiskey
# 23      X     X-ray
# 24      Y    Yankee
# 25      Z      Zulu

# 2. Convert dataframe to dictionary, identify why this will not work

phonetic_dict = data.to_dict()
print(phonetic_dict)
# {
#     'letter': {
#         0: 'A',
#         1: 'B',
#         2: 'C',
#         3: 'D',
#         4: 'E',
#         5: 'F',
#         6: 'G',
#         7: 'H',
#         24: 'Y',
#         25: 'Z'
#     },
#     'code': {
#         0: 'Alfa',
#         1: 'Bravo',
#         2: 'Charlie',
#         22: 'Whiskey',
#         23: 'X-ray',
#         24: 'Yankee',
#         25: 'Zulu'
#     }
# }

# Another way

data_df = pandas.DataFrame(phonetic_dict)
phonetic_dict = data_df.to_dict()
print(phonetic_dict)

# Nope, does not work, same flawed formatting, will not work

# 3. Create a dictionary using the NATO phonetic alphabet format

# formulas -
# new_dict = {new_key: new_value for item in list/range/tuple if test}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

for (k, v) in phonetic_dict.items():
    print(k)
    print(v)

# letter
# {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
#  14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
# code
# {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', 3: 'Delta', 4: 'Echo', 5: 'Foxtrot', 6: 'Golf', 7: 'Hotel', 8: 'India',
#  9: 'Juliet', 10: 'Kilo', 11: 'Lima', 12: 'Mike', 13: 'November', 14: 'Oscar', 15: 'Papa', 16: 'Quebec', 17: 'Romeo',
#  18: 'Sierra', 19: 'Tango', 20: 'Uniform', 21: 'Victor', 22: 'Whiskey', 23: 'X-ray', 24: 'Yankee', 25: 'Zulu'}

for (k, v) in data_df.items():
    print(k)
    print(v)

# letter
# 0     A
# 1     B
# 2     C
# Name: letter, dtype: object
# code
# 0         Alfa
# 1        Bravo
# 2      Charlie
# Name: code, dtype: object

for (index, rows) in data_df.iterrows():
    print(rows.letter)
# A
# B
#
# X
# Y
# Z

for (index, rows) in data_df.iterrows():
    print(rows.code)

# Alfa
# Bravo
# Charlie
#
# Yankee
# Zulu

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data_df.iterrows()}
print(new_phonetic_dict)

# {
#     'A': 'Alfa',
#     'B': 'Bravo',
#     'C': 'Charlie',
#     'U': 'Uniform',
#     'V': 'Victor',
#     'W': 'Whiskey',
#     'X': 'X-ray',
#     'Y': 'Yankee',
#     'Z': 'Zulu'
# }

# Beautiful

# 4. Create a list of the phonetic code words from the words that the user inputs

user_input = input('Enter your word: ').upper()
# formula - new_list = [do_this for item in list]
output = [new_phonetic_dict[i] for i in user_input]
print(output)

# Enter your word: Mobeen
# ['Mike', 'Oscar', 'Bravo', 'Echo', 'Echo', 'November']

# Done


# 243 Solution & Walkthrough for the NATO Alphabet Project

# Put it all together

import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_df = pandas.DataFrame(data)
# Not just from dictionary, the method apparently can also convert from csv data
# We could also just directly use data, it is a dataframe object

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}

user_input = input('Enter your word: ').upper()
output = [new_phonetic_dict[i] for i in user_input]
print(output)


# fin