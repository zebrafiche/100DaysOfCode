# 136 Installing Python Locally on Your Computer

# We are gonna be building a coffee machine later
# IDE - Integrated Development Environment
# Pycharm

# Before installing pycharm, install python


# 137 Download PyCharm for Windows or Mac

# Download the community version, since it is free


# 138 PyCharm's Charming Features (while you wait for the download to finish)

# Pycharm has some cool features

# 1. Spell check for english
# 2. Open another code file while coding for easy referring
# 3. Linter - Identify bits of code that might not be in accordance with the style guide
# The common style guide is pep8
# Example -
def my_function(n1, n2):
    total = n1 + n2
    return total


my_function(4, 5)

# 4. View Local History
# File > Local History > Show History

# 5. View Structure
# In the left pane, at the bottom, click structure

# 6. Refactor Rename
my_function(10, 11)
# Now let's say that I have decided to rename the function my_function()
# I would have to go back and individually change the name of the function and everytime I called it
# Click the function where it has been defined > Refactor > Rename


# 139 How to Install PyCharm on Windows

# Now that you have PyCharm installed, go ahead and File > New Project
# This will create a new folder, specify the folder path and name (maybe name the folder the project name?)
# Inside the project folder, a .py file will be auto created, by the name of main.py
# This is where your code will go


# 140 Installing PyCharm on Mac


# 141 Introduction & Requirements for the Coffee Machine Project

# 1. Print Report
# 2. Check sufficient resources?
# 3. Process Coins
# 4. Check transaction successful?
# 5. Make Coffee, adjust the resources and money


# To do tracking in PyCharm
# In the tab at the bottom, it will track your todos
# You just have to write it in a specific syntax and the tab will capture it

# TODO 1. Print Report
# TODO 2. Check sufficient resources?
# TODO 3. Process Coins
# TODO 4. Check transaction successful?
# TODO 5. Make Coffee, adjust the resources and money


# 142 Solution & Walkthrough for the Coffee Machine Code

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
#  dispensed. The prompt should show again to serve the next customer.

user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt

coffee_machine = True
while coffee_machine:

    if user_choice == 'off':
        coffee_machine = False

# TODO 3. Print report
# When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

if user_choice == 'report':
    for item in resources:
        if item != "Money":
            print(item, ':', resources[item], 'ml')
        else:
            print(item, ':', resources[item])

# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

for item in MENU[f"{user_choice}"]["ingredients"]:
    if MENU[f"{user_choice}"]["ingredients"][f"{item}"] > resources[f"{item}"]:
        print(f"Sorry there's not enough {item}")

# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

money_inserted = 0

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}

for i in coins:
    money_inserted += (int(input(f"how many {i}?: ")) * coins[f"{i}"])

# TODO 6. Check transaction successful?

if money_inserted < MENU[f"{user_choice}"]["cost"]:
    print("Sorry that's not enough money. Money refunded")
else:
    if money_inserted >= MENU[f"{user_choice}"]["cost"]:
        resources["money"] += money_inserted
        change_amount = float(money_inserted - MENU[f"{user_choice}"]["cost"])
        print(f"Here's {change_amount} in change")

# TODO 7. Make Coffee

for j in resources:
    resources[f"{j}"] = resources[f"{j}"] - MENU[f"{user_choice}"]["ingredients"][f"{j}"]

# Now put it together

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_inserted = 0

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}

resources["money"] = 0

coffee_machine = True
while coffee_machine:
    money_inserted = 0
    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_choice == 'report':
        for item in resources:
            if item != "money":
                print(item, ':', resources[item], 'ml')
            else:
                print(item, ':', resources[item], 'USD')
    elif user_choice == 'off':
        coffee_machine = False
    else:
        for i in coins:
            money_inserted += (int(input(f"how many {i}?: ")) * coins[i])

        if money_inserted < MENU[f"{user_choice}"]["cost"]:
            print("Sorry that's not enough money. Money refunded")
        else:
            # if money_inserted >= MENU[f"{user_choice}"]["cost"]:
            resources["money"] += MENU[f"{user_choice}"]["cost"]
            change_amount = round(money_inserted - MENU[f"{user_choice}"]["cost"], 2)
            print(f"Here's {change_amount} in change")

            ingredients_sufficient = True
            while ingredients_sufficient:
                for item in MENU[f"{user_choice}"]["ingredients"]:
                    if MENU[f"{user_choice}"]["ingredients"][f"{item}"] > resources[f"{item}"]:
                        print(f"Sorry there's not enough {item}")
                        resources["money"] -= MENU[f"{user_choice}"]["cost"]
                        print(f"Here's your {MENU[f'{user_choice}']['cost']} in change")
                        ingredients_sufficient = False
                    else:
                        # for j in resources:
                        # this is not needed, the loop will continue either way
                        resources[f"{item}"] = resources[f"{item}"] - MENU[f"{user_choice}"]["ingredients"][f"{item}"]
                print(f"Here's your {user_choice}. Enjoy")

# 143 Location, Location, Location - Pavlov's Coding Corner
