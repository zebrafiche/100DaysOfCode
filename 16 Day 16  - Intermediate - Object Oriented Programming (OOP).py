
# 144 Why do we need OOP and how does it work_

# Sometimes we get feelings like why our code is working as things get more complex
# The way we do now is called Procedural Programming

# Now let's imagine that you are building code for a self-driving car
# It's complex
# What if you broke the problem down?
# Camera Module, Lane Detection Module, Navigation Module, Fuel Management
# Imagine you have a whole team who are working on different modules?
# More productive
# A lot of these modules individually are reusable
# This modularizing is done using OOP

# What exactly is OOP?
# Imagine you run a restaurant, which you inherited from uncle
# Tasks - Reception, Reservation, Order Collect, Prepare, Delivery, Clean
# If you have a team, it gets easier



# 145 How to use OOP_ Classes and Objects

# Refer to the restaurant example
# Let's say we are going to model a waiter

# We have to define what it has and what it does

# has (attributes)
is_holding_plate = True
tables_responsible = [4, 5, 6]
# does (methods)
def take_order(table, order):
    # takes order to chef
def take_payment(amount):
    # add money to restaurant

# attributes are basically a variable that's associated with our modelled object, waiter
# it is not a free floating variable, it's not in our main.py, it's in fact attached to the object, waiter
# Similarly, method is a function for the modelled object specifically, not free floating functions
# for example, .append() is a method specifically for lists, they are not free to be used everywhere

# In OOP, we are trying to model real life objects that have things(attributes) and can do things(methods)
# Object is a way of combining some data and some functionality altogether in the same thing

# Once we have our object, we can generate multiple forks/versions of the object
# We can generate as many versions/forks we want (TachiyomiJ2K) from the same blueprint(Tachiyomi)
# In OOP, this blueprint is called "class"



# 146 Constructing Objects and Accessing their Attributes and Methods

# The blueprint is the code(git) and from the blueprint we can create as many objects as we want (Tachiyomi, TachiyomiJ2K)
# The object is the actual thing that we are going to be using in our code(e.g. interactive comics app)

# The code equivalent is this
car = CarBlueprint()
# (written with the first letter of each word capitalized, known as pascalcase)
# (to differentiate it from all other variables and objects, written with underscores)
# car is the object and CarBlueprint() is the class

# To see it in action, we are going to use a library.
# Library is code that someone else has written

# The library is called Turtle Graphics, comes preloaded with Python

# So in this case we are going to create an object(visual) from a blueprint(Turtle) that someone else has created

# The benefit for creating separate project folders is that if we have to create a module ourselves to be used here
# Like hangman_art.py, we can do this neatly
# Projects > Right-click on the project folder > Create new .py file(your module)
# import that module here

import new_module
print(new_module.new_variable)
# 12

# We want to do the same thing using turtle
# We want to tap into the class called Turtle inside this turtle module

import turtle
turtle.Turtle()
# you see that in the pop-up it shows that Turtle() is a class, denoted by a small c
# save it as your object
timmy = turtle.Turtle()

# we could also do it this way
from turtle import Turtle
timmy = Turtle()
print(timmy)
# <turtle.Turtle object at 0x0000014BBC8183D0>

timmy.shape("turtle")
timmy.color("Coral")
timmy.forward(100)

# Now what could we do with this object?
# Object Attributes

# the syntax for calling attributes is like below
# car_object.speed_attribute

# there is another class called screen in the turtle module, import that

from turtle import Screen
# the screen represents the window in which the turtle is going to show up
my_screen = Screen()

# my_screen is my object
# now call on the attributes called canvas height and width
print(my_screen.canvheight)
# 300

# Object Methods
# you call on methods by the same syntax you use to call on attributes
# methods are nth but functions, but since they are tied to an object they are called methods

my_screen.exitonclick()
# now run the code (multiline string the previous notes)
# you can see that a window pops up (h = 300, w = 300) and it shows an arrow in the middle(timmy the turtle)

# let's change timmy's shape from a cursor to a turtle
# timmy.shape("turtle")
# this print statement should go before you print the canvas

# let's change timmy's color from a cursor to a turtle
# timmy.color("CadetBlue1")
# this should also go before you print the canvas

# Now move the turtle 100 paces
# timmy.forward(100)
# Same, this should also go before you print the canvas

# So far we have seen object attributes
# my_screen.canvheight
# and methods
# timmy.shape("turtle")
# timmy.color("Coral")
# timmy.forward(100)



# 147 How to Add Python Packages and use PyPi

# How to integrate public packages and libraries into your project
# So we can create objects with attributes and methods?

# We have seen modules where each file we create in our project is essentially a module in itself
# For example, new_module.py

# But a package is different. It is basically made of lots of modules created by multiple people for a specific purpose.

# Let's say we want to create a table of Pokemons and their type
# We can do it by simple printing the characters one by one, line by line
# Cumbersome

# Or we could look for packages others have created

# Enter PyPi, the largest index of python packages on the web

# Go to PyPi
# Search for prettytable
# Install the package into our project (Settings > Project > Python Interpreter > +(bottom) > search and install)

# We can now access this package in our code
import prettytable
# If you want to see the documentation of prettytable, right click > go to > implementation
# For now we only need the documentation to understand how to use it



# 148 Practice Modifying Object Attributes and Calling Methods

from prettytable import PrettyTable
# do all libraries come with a class by the same name, only denoted with Titlecase?

# now create an object from this prettytable class
# From the documentation (and just like before) -
table = PrettyTable()
print(table)
# ++
# ||
# ++
# ++

# Now add data to it
# From the documentation -
# You can add data one column at a time as well. To do this you use the add_column method, which takes two arguments -
# a string which is the name for the field the column you are adding corresponds to,
# and a list or tuple which contains the column data:
#
# x.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])

table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
print(table)

# +--------------+----------+
# | Pokemon Name |   Type   |
# +--------------+----------+
# |   Pikachu    | Electric |
# |   Squirtle   |  Water   |
# |  Charmander  |   Fire   |
# +--------------+----------+


# Now change the alignment, which is an attribute (because no new things will be added, existing code will run)
# From the documentation -
# You can change the alignment of all the columns in a table at once by assigning a one character string to the align attribute.
# The allowed strings are "l", "r" and "c" for left, right and centre alignment, respectively:
#
# x.align = "r"
# print(x)

table.align = 'l'
print(table)

# +--------------+----------+
# | Pokemon Name | Type     |
# +--------------+----------+
# | Pikachu      | Electric |
# | Squirtle     | Water    |
# | Charmander   | Fire     |
# +--------------+----------+



# 149 Building the Coffee Machine in OOP

# Steve Jobs explained OOP very well once
# Let's say you are in Kolkata and you need you shirt washed
# You don't have Rupees
# You do not know Hindi
# You could, like learn these and then do this yourself
# Or, you could go to the hotel you are staying at and ask them to help you
# So in OOP that would be
# hotel.dryclean()

# In the last lesson we made the coffee machine from scratch, kinda like learning Hindi and geting Rs ourselves
# Let's. like hotel.dryclean(), use OOP to do that

# Coffee Machine


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Todo 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer

# create an object
drink = Menu()
print(Menu().get_items())
# latte/espresso/cappuccino

choice = input(f"What would you like? ({Menu().get_items()}): ")

# a. check the user's input
user_drink = Menu().find_drink(choice)


# b. The prompt should show every time action has completed
is_machine_on = True
while is_machine_on:
    # Now the code you have written above


# Todo 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
# machine. Your code should end execution when this happens.

if choice == 'off':
    is_machine_on = False


# Todo 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows the
# current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

maker = CoffeeMaker()
maker.report()
money.report()

# Todo 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough resources
# to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not
# continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


if maker.is_resource_sufficient(choice):
    # make coffee
else:
    print('Sorry there is not enough ingredient')


# Todo 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

money = MoneyMachine()
money.make_payment()


# Todo  6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected. E.g
# Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program
# should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.

if money.make_payment():

else:
    print('Sorry that is not enough money. Money refunded.')


# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the user
# selected, then the ingredients to make the drink should be deducted from the coffee
# machine resources

maker.make_coffee(drink.find_drink(choice))



# Put it together

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drink = Menu()
# print(Menu().find_drink('latte').name)
# print(Menu().find_drink('latte').cost)
# print(Menu().find_drink('latte').ingredients)

mymenu = Menu()
machine = CoffeeMaker()
funds = MoneyMachine()

is_machine_on = True
while is_machine_on:
    choice = input(f"What would you like? ({mymenu.get_items()}): ")
    if choice == 'off':
        is_machine_on = False
    elif choice == 'report':
        machine.report()
        funds.report()
    else:
        user_drink = mymenu.find_drink(choice)
        if machine.is_resource_sufficient(user_drink):
            if funds.make_payment(user_drink.cost):
                machine.make_coffee(user_drink)
                # print("Here is your latte. Enjoy!")
            else:
                print('Sorry that is not enough money. Money refunded.')
        # else:
        #     print('Sorry there is not enough ingredient')


# 150 Walkthrough and Solution for the OOP Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mymenu = Menu()
machine = CoffeeMaker()
funds = MoneyMachine()

s_machine_on = True
while is_machine_on:
    choice = input(f"What would you like? ({mymenu.get_items()}): ")
    if choice == 'off':
        is_machine_on = False
    elif choice == 'report':
        machine.report()
        funds.report()
    else:
        user_drink = mymenu.find_drink(choice)
        if machine.is_resource_sufficient(user_drink):
            if funds.make_payment(user_drink.cost):
                machine.make_coffee(user_drink)


# 151 Don't forget to review occasionally
