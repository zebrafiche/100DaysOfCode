print('Hello World')
##Hello World
##Going through Lesson 7 of Day 1

print('Day 1 - Python print function \nThe function is declared like this \nprint(\'what to print\')')
##Day 1 - Python print function 
##The function is declared like this 
##print('what to print')


print('Day 1 - Python print function \nThe function is declared like this')
print("print('what to print')")
##Day 1 - Python print function 
##The function is declared like this
##print('what to print')

##So now you know a use of the double quotes
##Python does not really care if you have enclosed in single or double code, as long as it is enclosed, it is considered a string

##What if I wrote it like this?
##print("print("what to print")")
##The second double quotes would have been considered the closing of the string and the rest (what to print")")) would confuse Python





##Lesson 08 - String Manipulation and Code Intelligence

# Print 'Hello World' three times using the \n
print('Hello World\nHello World\nHello World')
# Hello World
# Hello World
# Hello World

# Concatenating strings
# Plus sign prints without the space 
print('Hello' + 'Angela')
# HelloAngela

# Remember about spaces at the beginning of a line of code. If they happen to be anywhere they are not supposed to be, you will get an indentation error 

# When you have code intelligence turned on in the text editor, it gives you squiggly red lines the moment you start writing something that has an error 




# Lesson 09 [Interactive Coding Exercise] Debugging Practice

# print the following
# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

print('Day 1 - String Manipulation\nString Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")\nNew lines can be created with a backslash and n.')
# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.


# 010 The Python Input Function

input('What is your name? ')
# What is your name? and the cursor stays there expecting an input
# it is a prompt for the user

# Now when you nest an input() inside a print()
print('Hello', input('What is your name? '))
# Hello Rafi



# 011 [Interactive Coding Exercise] Input Function

print(len(input('What is your name?')))
# What is your name? John Steinbeck
# 15

# I have started typing preceding with a space. This seems to have calculated the space too. 



# 012 Python Variables

# 013 [Interactive Coding Exercise] Variables

# Instructions
# Write a program that switches the values stored in the variables a and b. 

a = input('a = ')
b = input('b = ')

a, b = b, a 

print('a =', a)
print('b =', b)

# a = 5
# b = 7
# a = 7
# b = 5


# 014 Variable Naming

# 015 Day 1 Project_ Band Name Generator

print('Hello, welcome to the band name generator')
m = input('What is the name of the city you grew up in?\n')
n = input('What is the name of your favorite pet?\n')
print('Your band name could be', m, n)


# Day 1 Done 