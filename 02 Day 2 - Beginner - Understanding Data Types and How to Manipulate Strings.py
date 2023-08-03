# 017 Day 2 Goals_ what we will make by the end of the day
# By the end of the day we will have learnt how to build a tip calculator

# Let's do it my way
print('Welcome to the tip calculator')
tb = int(input('What was the total bill? '))
p = int(input('How many people are you going to split the bill to? '))
tp = int(input('What percentage of tip do you wanna pay? 10? 20? '))
d = tb*(1+(tp/100))/p
print('Each person should pay', d)

# Welcome to the tip calculator
# What was the total bill? 100
# How many people are you going to split the bill to? 10
# What percentage of tip do you wanna pay? 10? 20? 100
# Each person should pay 20.0




# 018 Python Primitive Data Types

# You already know about strings 

# When you write numbers, if you put underscores in between Python ignores it 
print(123_456_789)
# 123456789

# All whole numbers all called integers in programming
# Numbers with decimals are called float 
# Because the decimal point can float around the number, being able to be at any point 

# Then there is booleans, True and False data types 




# 019 Type Error, Type Checking and Type Conversion 

# What will this line of code print?
print(70 + float('100.5'))
# we are taking a string, converting it into float and then adding it to an integer
# 170.5


# 020 [Interactive Coding Exercise] Data Types

m = input('Type a two digit number - ')
n = int(m[0]) + int(m[1])
print(n) 


# 021 Mathematical Operations in Python

# When you have multiple mathematical operation in a function, the order followed is not BODMAS
# It's PEMDAS
# Parenthesis
# Exponents
# Multiplication
# Division
# Addition
# Subtraction
# This runs from left to right of the function

print(3*3+3/3-3)
# 7.0

# How can we change the line of code so that we get 3.0?

print(3*3/3+3-3)
# 3.0

# Now without changing order of the operators?
print(3*(3+3)/3-3)
# 3.0


# 022 [Interactive Coding Exercise] BMI Calculator

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# **Warning** you should convert the result to a whole number.

w = float(input('What is your weight? - '))
h = float(input('What is your height? - '))

bmi = int(w/h**2)
print(bmi)
# 27


# 023 Number Manipulation and F Strings in Python

# Round
print(round(8/3))
# 3

# Round to two decimal points
print(round(8/3, 2))
# 2.67

# Floor division
print(8//3)
# 2

score  = 100
height = 1.8
isWinning = True

# How to combine these data above of multiple types into one string without converting?

# F string
# just like raw text (r''), we use we wrap the concatenation into f'' and put the different types inside curly braces
# all the converting will be done in the backend
print(f'your score is {score}, and your height is {height}')
# your score is 100, and your height is 1.8


# 024 [Interactive Coding Exercise] Life in Weeks

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
# It will take your current age as the input and output a message with our time left in this format:
# > You have x days, y weeks, and z months left. 
# Where x, y and z are replaced with the actual calculated numbers. 

age = int(input('What is your age? - '))
ml = (90- age)*12
wl = ml*4
dl = wl*7

print(f'You have {dl} days, {wl} weeks and {ml} months left to live. Live bigger')
# You have 19152 days, 2736 weeks and 684 months left to live. Live bigger

# Watch the video still, you might learn sth new



# 025 Day 2 Project_ Tip Calculator

print('Welcome to the Tip Calculator')
totalbill = float(input('What was the total bill? BDT'))
tip = float(input('What percentage of tip would you like to give?'))
n = int(input('How many people to split the bill?'))
payment = round(totalbill*(1+tip/100)/n, 2)
print(f'Each person should pay BDT {payment}')
# Each person should pay BDT 11.0