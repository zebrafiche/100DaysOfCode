# 057 Day 6 Goals_ what we will make by the end of the day 

# We will make use of something called Karel the robot to understand complex concepts 
# By the end of the day, we wiil make a maze game, and our robot will be able to solve it 




# 058 Defining and Calling Python Functions 

# To learn all types of python built in functions, visit - https://docs.python.org/3/library/functions.html 
# We denote functions by its name followed by a set of parenthesis 

# How to make your own function? 
def my_function():
# like all other functions, customized functions should also contain parenthesis

# In programming lingo, using the function is called calling the function

# Suppose you want to ask your robot to pick up some milk
# You cannot just tell it do so right?
# You gotta give it specific instruction, go right, left, enter, pay, pick etc.
# Wrting these everyday to make it work everyday
# But with functions (def), you can store all these instructions in one place and just call the function

# Reeborg's world, a simulation to help learn python 
# Link - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json 

# Task on reeborg's world - make a function that makes the robot turn right 




# 059 The Hurdles Loop Challenge

# Reeborg's world challenge, go to the world named Hurdles 1 
# Make reeborg pass through all of the obstacles
# This is where you use the def keyword, define the code it takes to pass one obstacle
# And then repeat for 6 obstacles using def

# To make the def function run your desired number of times, use for loop 

# Example - 

def song():
    print('Eat')
    print('Sleep')
    print('Wake')
    print('Thinking about you')

for i in range(1, 4):
    song()

# Eat
# Sleep
# Wake
# Thinking about you
# Eat
# Sleep
# Wake
# Thinking about you
# Eat
# Sleep
# Wake
# Thinking about you





# 060 Indentation in Python 

def my_function():
    print('Hello')
    print('World')
my_function()
# Hello
# World





# 061 While Loops

# while something is True:
#     do something repeatedly

# while loops vs for loops 
# if you are iterating over a list, and have different iterables every time:
#     use a for loop
# if your iterable is the same:
#     use the while loop (though for loop can also be chosen)

# Reeborg's world World 2 puzzle:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def obstacle_run():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    obstacle_run()

# while loops can easily turn into infinite loops





# 062 Hurdles Challenge using While Loops

# Reeborg has entered a hurdle race. Make him run the course, following the path shown.

# The position and number of hurdles changes each time this world is reloaded.
# What you need to know

#     The functions move() and turn_left().
#     The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#     How to use a while loop and an if statement.

# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def obstacle_run():
    #move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        obstacle_run()





# 063 Jumping over Hurdles with Variable Heights

# Reeborg has entered a hurdle race. Make him run the course, following the path shown.

# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know

# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and combine them for this last hurdles race.

# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def obstacle_run():
    #move()
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        obstacle_run()




# 064 Final Project_ Escaping the Maze

# Reeborg was exploring a dark maze and the battery in its flashlight ran out.

# Write a program using an if/elif/else statement so Reeborg can find the exit. 
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, 
# going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know

#     The functions move() and turn_left().
#     Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
#     How to use a while loop and if/elif/else statements.
#     It might be useful to know how to use the negation of a test (not in Python).

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while at_goal() == False:
    while right_is_clear():
        turn_right()
        if front_is_clear():
            move()
        else: 
            turn_left()
    while wall_on_right():
        if front_is_clear():
            move()
        else: 
            turn_left()

# This here code gets into an infinite loop with some unique cases 
# Debugging required
# Come back for the second part of this video once you have completed Day 15





# 065 Why is this _so_ Hard_! Can I really do this_