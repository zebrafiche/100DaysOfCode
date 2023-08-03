# 122 Describe the Problem

# How to find and get rid of bugs 

# Describe the problem

def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# nothing gets printed, why?
# i takes on various values between 1 and 20. However, when i reaches 20, nth gets printed 

# Assumption - i reaches 20

# Fix 

def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# You got it





# 123 Reproduce the Bug

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Sometimes it produces an error 

# We will try to reproduce the error by changing the part of the code that does not stay constat
dice_num = randint(1, 6)
# This line does not stay constant, it changes value everytime we run the code 

# change the code to dice num = 1 and run, and do it all the way up to 6

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6
print(dice_imgs[dice_num])

# IndexError: list index out of range

# Fix 

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# works now 





# 124 Play Computer and Evaluate Each Line

# Pretend that you are the computer and go through each line of code 

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Which part of your code changes
year = int(input("What's your year of birth?"))

# What happens if year is 1994

# nothing 
# there's your bug

# Fix 

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# You are a Gen Z.




# 125 Fixing Errors and Watching for Red Underlines

age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

# See the red underline under print? Fix it 

age = input("How old are you?")
if age > 18:
  print("You can drive at age {age}.")

# TypeError: '>' not supported between instances of 'str' and 'int'

# Part of the code that changes - 
age = input("How old are you?")

# Fix it 
age = int(input("How old are you?"))
if age > 18:
  print("You can drive at age {age}.")

# You can drive at age {age}

# Bug again
# Now look at the parts where it is constant, these are harder to debug

# Fix 
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

# You can drive at age 21.




# 126 Squash bugs with a print() Statement

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# 0
# Why

# Use print()

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page == int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)


# print(word_per_page) gives 0 no matter what we enter as input 

# Fix 

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
# 2
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
# 20
total_words = pages * word_per_page
print(total_words)
# 40




# 127 Bringing out the BIG Gun_ Using a Debugger

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# 26
# just 26, why?

# Use thonny or pythontutor.com to see the debugger in action 

# In pythontutor.com, click on a line to create a breakpoint there
# The code stops there and you can examine what happens in that particular line

# We can see that b_list only appends the last value of the initial list 
# Issue - no indent 

# Fix 
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# [2, 4, 6, 10, 16, 26]

# Now in pythontutor you can see that your previous breakpoint now gets executed 6 times 
# The debugger is like a print() statement in all the lines of code, helps you to isolate the problem area 





# 128 Final Debugging Tips

# Take a break, have a nap, have a break
# Ask a friend, maybe a developer
# Run often, meaning run your code often after every few lines, so you can catch the bugs as they form early on
# Ask StackOverflow




# 129 [Interactive Coding Exercise] Debugging Odd or Even

number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


# Fix 

number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")





# 130 [Interactive Coding Exercise] Debugging Leap Year

year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


# Fix 

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")



# 131 [Interactive Coding Exercise] Debugging FizzBuzz

for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

# Fix 

for number in range(1, 101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)



# 132 Building Confidence