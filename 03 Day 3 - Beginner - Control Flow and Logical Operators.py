# 027 Day 3 Goals_ what we will make by the end of the day

# We will be making a text based adventure game



# 028 Control Flow with if _ else and Conditional Operators

# if/else statements
# for flow charts, visit draw.io 



# 029 [Interactive Coding Exercise] Odd or Even_ Introducing the Modulo

# Write a program that works out whether if a given number is an odd or even number. 
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is **even** because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is **odd** because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The **modulo** is written as a percentage sign (%) in Python. It gives you the remainder after a division.

num = float(input())
if num%2 == 0:
    print('Even')
else:
    print('Odd')



# 030 Nested if statements and elif statements


# 031 [Interactive Coding Exercise] BMI 2.0

height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))
bmi = weight/height**2

if bmi < 18.5:
    print(f'You bmi is {bmi}, meaning you are underweight')
elif 18.5 < bmi < 25:
    print(f'You bmi is {bmi}, meaning you are of normal weight')
elif 25 < bmi < 30:
    print(f'You bmi is {bmi}, meaning you are overweight')
elif 30 < bmi < 35:
    print(f'You bmi is {bmi}, meaning you are obese')
else:
    print(f'You bmi is {bmi}, meaning you are clinically obese')


# 032 [Interactive Coding Exercise] Leap Year 

# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year. 

# > `on every year that is evenly divisible by 4
# >   **except** every year that is evenly divisible by 100
# >     **unless** the year is also evenly divisible by 400

year = int(input('What year do you want to check?: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not a leap year man')
    else:
        print('Leap year guy')
else:
    print('Not a leap year')


# 033 Multiple If Statements in Succession

# if:
#     do A 
# elif:
#     do B 
# else:
#     do C
# this is where only one condition is carried out


# if:
#     do A 
# if:
#     do B 
# if:
#     do C 
# this is where all three conditions can be carried out


# 034 [Interactive Coding Exercise] Pizza Order Practice 

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. 

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y':
    bill += 1
print(f'Your total bill is {bill}')




# 035 Logical Operators

# if condition1 and condition2 and condition3:
#     do this
# else:
#     do this

Logical operators - 

# A and B
# C or D
# not E


# 036 [Interactive Coding Exercise] Love Calculator 

# You are going to write a program that tests the compatibility between two people.  
# To work out the love score between two people:

# > Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 

# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."` 

# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:
# `"Your score is **z**."`

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# # Hint
# 1. The `lower()` function changes all the letters in a string to lower case. 
# 2. The `count()` function will give you the number of times a letter occurs in a string. 

score = 0

newname  = (name1 + '' + name2)
lower_names = newname.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))



if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score > 40 and score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}')

# Welcome to the Love Calculator!
# name1 = Catherine Zeta-Jones
# name2 = Michael Douglas
# Your score is 99, you go together like coke and mentos.



# 037 Day 3 Project_ Treasure Island 

# for the flowchart - 'https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload'

print('Welcome to the treasure island. Your mission is to find the treasure')
lr = input('left or right?\n')
if lr == 'left':
    sw = input('swim or wait?')
    if sw == 'wait':
        d = input('which door? name a color')
        if d == 'red':
            print('burned by fire, game over')
        elif d == 'blue':
            print('eaten by beasts, game over')
        elif d == 'yellow':
            print('you win')
        else:
            print('game over')
    else:
        print('attacked by trout, game over')
else:
    print('fall into a hole, game over')
