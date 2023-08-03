# 097 Day 10 Goals_ what we will make by the end of the day

# By the end of the day, we will build a calculator




# 098 Functions with Outputs

# We already know a few things about functions
# Now there is another type of function, that has an output
def my_function():
    result = 3*2
    return result
# So now when we call the function we get an output "result"
# This can be stored in a variable

def format_name(f_name, l_name):
    # We are going to make the names titlecase
    firstname = f_name.title() 
    lastname = l_name.title()
    return f"{firstname} {lastname}"
    # Now instead of printing we could also return the output
formatstring = format_name('abdullah', 'rafi')
print(formatstring)
# Abdullah Rafi

# We can visualize this better with Thonny

# Diff between "print" and "return" - 
# for example the len() function does not print the length, it stores it of sorts
# the return keyword is the most imp thing for functions that has an output




# 099 Multiple return values

def format_name(f_name, l_name):
    # We are going to make the names titlecase
    firstname = f_name.title() 
    lastname = l_name.title()
    return f"{firstname} {lastname}"
    print('this got printed')

print(format_name('abdullah', 'rafi'))
# Abdullah Rafi
# The next line never gets printed

# The return keyword effectively ends the function, wherever it is

# For example, we want to bypass the function if the user types nothing in parameters, so no firstname or lastname
def format_name(f_name, l_name):
    # We are going to make the names titlecase
    if f_name == "" or l_name == "":
        return 
    firstname = f_name.title() 
    lastname = l_name.title()
    return f"{firstname} {lastname}"

print(format_name(input('first name? '), input('last name? ')))

# first name? RAFI
# last name? ABDULLAH
# Rafi Abdullah

# first name? 
# last name?
# None

def format_name(f_name, l_name):
    # We are going to make the names titlecase
    if f_name == "" or l_name == "":
        return "You dodn't provide valid inputs"
    firstname = f_name.title() 
    lastname = l_name.title()
    return f"{firstname} {lastname}"

print(format_name(input('first name? '), input('last name? ')))

# first name? 
# last name?
# You dodn't provide valid inputs



# 100 [Interactive Coding Exercise] Days in Month

# In the starting code, you'll find the solution from the Leap Year challenge. 
# First, convert this function `is_leap()` so that instead of printing "Leap year." or "Not leap year." 
# it should **return** `True` if it is a leap year and **return** `False` if it is not a leap year.

# You are then going to create a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.
# days_in_month(year=2022, month=2)
# ```

# And it will use this information to work out the **number of days in the month**, 
# then **return** that as the **output**, **e.g.:**

# ```
# 28
# ```

# The List month_days contains the number of days in a month from January to December for a non-leap year. 
# A leap year has 29 days in February.

# # Hint

# 1. Look at the function call at the bottom of the code to see the positional arguments.  
# The order is very important.

# 2. Feel free to choose your own parameter names.

# 3. Remember that `month_days` is a List and Lists in Python start at position 0. 
# So the number of days in January is `month_days[0]`

# 4. Be careful with indentation.


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month_days == 2:
     return 29
#   else: no else statement required, the previous return won't be executed if it's not a leap year
  return month_days[month-1]
     
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Alternative code improving user experience

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
     return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month_days == 2:
     return 29
  return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Question - Why return at all, why not just do a print statement? It is basically doing the same thing




# 101 Docstrings

# Docstrings are basically a way for us to create little bits of documentation as we're coding along
# in our functions or in our other blocks of code.

# For example the len() function, as soon as you open up the parenthesis you see a little piece of documentation
# telling you what it does

# How to do the same for the functions we write? Docstrings

 
def format_name(f_name, l_name):
   """Take a first and last name and 
   format it in titlecase"""
# The docstring comes right after you define a function, and comes with three quotation marks

#  Now you can see that as you type format_name the description pops up, one that you wrote just now





# 102 Calculator Part 1_ Combining Dictionaries and Functions

# Challenge - create functions for the operations

def add(a, b):
   """Takes two parameters and adds them"""
   return a + b
def subtract(a, b):
   """Takes two parameters and minuses them"""
   return a - b
def multiply(a, b):
   """Takes two parameters and multiplys them"""
   return a * b 
def divide(a, b):
   """Takes two parameters and divides them"""
   return a / b


# Challenge - create a dictionary where the keys are the symbols above and the values are the names of the functions above

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

# Ask user for the numbers
num1 = int(input("What's the first number? "))

# Show them the operations 
for i in operations:
   print(i)
operation_symbol = input("What is the operation? ")

num2 = int(input("What's the second number? "))

calculation_function = operations[operation_symbol]
# calculation_function becomes add, for example
answer = calculation_function(num1, num2)
# and with add, we include parentheses and two arguments
print(f"{num1} {operation_symbol} {num2} is {answer}")
# finally print 




# 103 Print vs. Return

# What if your output for a function is the input for another function?
# Or maybe you wanna store the output in a variable to be used later?
# You won't be able to do those if you're doing print() instead of return



# Note - there was a bug spotted in this lesson, go to the debugging solution to see why it happens
# Basically the new symbol inputted by the user is store in calculation_function which overrides the previous calculation_function
# So the entire calculation is done with the new calculation_function




# 104 While Loops, Flags and Recursion

# How do we make the calculator ask the user if s/he wants to continue with the previous number or exit

continuecalc = True
def add(a, b):
   """Takes two parameters and adds them"""
   return a + b
def subtract(a, b):
   """Takes two parameters and minuses them"""
   return a - b
def multiply(a, b):
   """Takes two parameters and multiplys them"""
   return a * b 
def divide(a, b):
   """Takes two parameters and divides them"""
   return a / b

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

# Ask user for the numbers
num1 = int(input("What's the first number? "))

while continuecalc == True:
  # Show them the operations 
  for i in operations:
    print(i)
  operation_symbol = input("What is the operation? ")

  num2 = int(input("What's the next number? "))

  calculation_function = operations[operation_symbol]
  # calculation_function becomes add, for example
  answer = calculation_function(num1, num2)
  # and with add, we include parentheses and two arguments
  print(f"{num1} {operation_symbol} {num2} is {answer}")
  # finally print 


  repeat = input('Type "y" to calculate using the {answer}, otherwise "n" to exit')
  if repeat == "y":
    num1 = answer
  elif repeat == "n":
    continuecalc = False


# Now this above is if the user wants to continue with the previous answer
# What if he wanted to start another fresh calculation?


# Recursion 
# This is the idea of creating a function that calls upon itself where appropriate

# Create a new function named calculator and put everything so far inside that function 
def calculator():
   
  continuecalc = True
  def add(a, b):
    """Takes two parameters and adds them"""
    return a + b
  def subtract(a, b):
    """Takes two parameters and minuses them"""
    return a - b
  def multiply(a, b):
    """Takes two parameters and multiplys them"""
    return a * b 
  def divide(a, b):
    """Takes two parameters and divides them"""
    return a / b

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }

  # Ask user for the numbers
  num1 = int(input("What's the first number? "))

  while continuecalc == True:
    # Show them the operations 
    for i in operations:
      print(i)
    operation_symbol = input("What is the operation? ")

    num2 = int(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    # calculation_function becomes add, for example
    answer = calculation_function(num1, num2)
    # and with add, we include parentheses and two arguments
    print(f"{num1} {operation_symbol} {num2} is {answer}")
    # finally print 

# Change the final prompt a little bit so the user can start a fresh calculation 
    repeat = input('Type "y" to calculate using the {answer}, otherwise "n" to start a new calculation')
    if repeat == "y":
      num1 = answer
    elif repeat == "n":
      continuecalc = False
      # Finally call the function calculator so everything starts from the beginning again 
      # Since continuecalc = False the loop won't happen
      calculator()

# Be careful working with recursions, they can be an infinite loop 
# def name():
#    print("aaaargh")
#    name()
# this here will create an infinite loop






# 105 Calculator Finishing Touches and Bug Fixes

# Add the logo
# What happens when we try to enter a decimal point number?
# Can we try to use other operators? Like square root and such?

from calculatorart import logo
print(logo)

def calculator():
   
  continuecalc = True
  def add(a, b):
    """Takes two parameters and adds them"""
    return a + b
  def subtract(a, b):
    """Takes two parameters and minuses them"""
    return a - b
  def multiply(a, b):
    """Takes two parameters and multiplys them"""
    return a * b 
  def divide(a, b):
    """Takes two parameters and divides them"""
    return a / b

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }

  # Ask user for the numbers
  num1 = float(input("What's the first number? "))

  while continuecalc == True:
    # Show them the operations 
    for i in operations:
      print(i)
    operation_symbol = input("What is the operation? ")

    num2 = float(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    # calculation_function becomes add, for example
    answer = calculation_function(num1, num2)
    # and with add, we include parentheses and two arguments
    print(f"{num1} {operation_symbol} {num2} is {answer}")
    # finally print 

# Change the final prompt a little bit so the user can start a fresh calculation 
    repeat = input(f"Type 'y' to calculate using the {answer}, otherwise 'n' to start a new calculation")
    if repeat == "y":
      num1 = answer
    elif repeat == "n":
      continuecalc = False
      # Finally call the function calculator so everything starts from the beginning again 
      # Since continuecalc = False the loop won't happen
      calculator()

# And, call your function so that it does not stop after just printing the logo 

calculator()




# 106 How to Get a Good Night's Sleep