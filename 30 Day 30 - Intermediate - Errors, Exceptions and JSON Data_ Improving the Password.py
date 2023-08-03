# 268 Day 30 Goals_ what you will make by the end of the day

# Errors, exceptions and how to save and load JSON data
# We will look at some errors and how to avoid outright crashing of our app
# JSON is one of widely used formats to transfer data across internet between applications

# We will use it fine tune our password manager
# As an additional feature, we will be able to search for passwords too, we will type a website and hit search

# Some obvious errors that the app might undergo will be discussed and how to handle them without letting the app crash


# 269 Catching Exceptions_ The try catch except finally Pattern

# Usually, when an error happens, the entire program crashes, not just the part with the error
# Snippet of code in the password_manager.py file -
with open('pasmanager.txt', 'a') as passmanager:  # made a mistake, not "passmanager" but "pasmanager"
    # not a single line after this will execute, it won't write, let alone delete previous values from the entry widgets
    passmanager.write('\n')
    passmanager.write('\n')
    passmanager.write(website)
    passmanager.write('\n')
    passmanager.write(username)
    passmanager.write('\n')
    passmanager.write(password)
    site_entry.delete(0, tkinter.END)
    pass_entry.delete(0, tkinter.END)

# We will work with four main keywords when handling exceptions/errors -
try:
    # something that might cause an exception
except:
    # do this if there is an exception
else:
    # do this if there is not any exceptions
finally:
    # do this no matter what happens

# shortened form of the error above -
with open("a_file.txt") as file:
    file.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

# Now to bypass the error -
try:
    # something that might cause an exception
    file = open("a_file.txt")
    a_dictionary = {"Key": "Value"}
    print(a_dictionary["assdsdf"])

except FileNotFoundError:
    # do this if there is an exception
    # it is good practice to mention the error we are expecting
    # otherwise it would execute the exception for all kinds of errors, file specific or non file specific
    # if the file does not exist, we are going to create the file, by opening it in write or append mode
    file = open("a_file.txt", "a")
# use another exception for that KeyError
except KeyError as error_message:  # this is another way to write except, this gets hold of the error message for us
    print(f"The key {error_message} does not exist")
    # The key 'assdsdf' does not exist
else:
    # do this if there is not any exceptions
    content = file.read()
    print(content)
    # this else block will only execute if there exists no errors (FileNotFoundError or KeyError)

finally:
    # do this no matter what happens
    file.close()
    print("File was closed")


# 270 Raising your own Exceptions

# We can raise our own exceptions, or error messages
# Now why would we want to do that?

height = float(input("Height: "))
weight = int(input("Weight: "))
# what if someone types a height above 3 metres, which is a non human height tbh?
# raise an exception, otherwise the program would continue calculating bmi with wrong height
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


# 271 [Interactive Coding Exercise] IndexError Handling

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)
# IndexError: list index out of range

fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")
try:
    make_pie(4)
except IndexError as error_message:
    print(f"The {error_message} is the problem. Select something less than 3")

# OR

fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")

make_pie(4)


# 272 [Interactive Coding Exercise] KeyError Handling

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    total_likes = total_likes + post['Likes']

print(total_likes)

# KeyError: 'Likes'

# The code will crash and give you a **KeyError**.
# This is because some of the posts in the `facebook_posts` don't have any `"Likes"`.

# 1. You'll need to catch the KeyError exception.
# 2. Posts without any likes can be counted as 0 likes.

# Solution -

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes = total_likes + 0
        post['Likes'] = 0

print(total_likes)
print(facebook_posts)

# 86
# [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2, 'Likes': 0},
#     {'Comments': 1, 'Shares': 1, 'Likes': 0},
#     {'Likes': 19, 'Comments': 3}
# ]

# Alternatively -
except KeyError:
    pass


# 273 Code Exercise_ Exception Handling in the NATO Phonetic Alphabet Project

# A few days ago we did the "Nato Alphabet" project
# The code looked something like this -

import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_df = pandas.DataFrame(data)

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}

user_input = input('Enter your word: ').upper()
output = [new_phonetic_dict[i] for i in user_input]
print(output)

# A flaw in the code is that it relies on the user entering texts or strings
# What if the user inputs numbers?

# 1. Make it so that everytime the user enter anything other than names, he will be notified and the code will repeat

import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_df = pandas.DataFrame(data)

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}

is_on = True
while is_on:
    user_input = input('Enter your word: ').upper()
    try:
        output = [new_phonetic_dict[i] for i in user_input]
    except KeyError:
        print("Only letters in the alphabet please.")
    else:
        print(output)
        break

# Alternative method -

import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_df = pandas.DataFrame(data)

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}

def generate_phonetic():
    user_input = input('Enter your word: ').upper()
    try:
        output = [new_phonetic_dict[i] for i in user_input]
    except KeyError:
        print('Only letters in the alphabet please')
        generate_phonetic()
    else:
        print(output)

generate_phonetic()


# 274 Write, read and update JSON data in the Password Manager

# As of now the password manager code generates a new text file and saves all our entered password there
# Now we want to add a functionality, the ability to search upon entering the name of a website
# To see if the password for that website has already been entered before
# For that, we need to save the passwords into a file type named JSON

# Timestamp - 01:00

# JSON - Javascript Object Notation
# To work with JSON data with python, we use the inbuilt JSON library
# write to a JSON file - json.dump()
# read a JSON file - json.load()
# update JSON file - json.update()

# Writing to JSON

# before, in the password manager, the code was like this -
def add_click():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()

    # messagebox.showinfo(title="Success", message="Done")
    # instead of this, use the askokcancel method, it generates a boolean value if clicked ok/cancel
    # use that to record the info on the passmanager.txt

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please provide info in all of the fields.")
    else:
        is_ok = messagebox.askokcancel(title='Confirm', message=f'This is what you entered: \nSite: {website}, '
                                                                f'\nUsername: {username}, \nPassword: {password}')
        if is_ok:
            with open('passmanager.txt', 'a') as passmanager:
                passmanager.write('\n')
                passmanager.write('\n')
                passmanager.write(website)
                passmanager.write('\n')
                passmanager.write(username)
                passmanager.write('\n')
                passmanager.write(password)
                site_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)

# Now, if we want to export the data to a JSON file, we need to make some changes -
import json
def add_click():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    # create a new nested dictionary with website as key and username and pass as values
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # messagebox.showinfo(title="Success", message="Done")
    # instead of this, use the askokcancel method, it generates a boolean value if clicked ok/cancel
    # use that to record the info on the passmanager.txt

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please provide info in all of the fields.")
    else:
        is_ok = messagebox.askokcancel(title='Confirm', message=f'This is what you entered: \nSite: {website}, '
                                                                f'\nUsername: {username}, \nPassword: {password}')
        if is_ok:
            # create a new json file
            with open('passmanager.json', 'w') as passmanager:
                # dump the new dictionary into the json file
                json.dump(new_data, passmanager, indent=4)
                # indent= 4 so that the data dumped is formatted beautifully
                site_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)

# Upon testing it, we can see that a new json file named passmanager has been created, containing data like this -
# {"Amazon": {"username": "rough.rafi@gmail.com", "password": "x(3WziD(%PN$m4U"}}
# going back and adding indent=4 as a keyword argument formats the contents of the json file -
# {
#     "Amazon": {
#         "username": "rough.rafi@gmail.com",
#         "password": "ZI((y2CVGCu#rg27"
#     }
# }


# Loading from JSON
# use json.load with the file name as an argument, save it in a file
# open the file in read mode
with open('passmanager.json', 'r') as passmanager:
    # load the file, save it in a variable
    data = json.load(passmanager)
    # print it
    print(data)
    for k, v in data:
        print(k)
        print(v)
# this will print data in the console, as a dictionary


# Updating JSON
# open the json file in read mode
with open('passmanager.json', 'r') as passmanager:
    # load the file, save it in a variable
    data = json.load(passmanager)
    # update the data with new_data which is the dictionary with the new parameters
    data.update(new_data)
    # so data is now updated, contains both the old dictionary and the new dictionary
    # store that data back into the json, but first open the file in write mode
with open('passmanager.json', 'w') as passmanager:
    json.dump(new_data, passmanager, indent=4)

# So adding all the functionalities in the code results in -

def add_click():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    # create a new nested dictionary with website as key and username and pass as values
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # messagebox.showinfo(title="Success", message="Done")
    # instead of this, use the askokcancel method, it generates a boolean value if clicked ok/cancel
    # use that to record the info on the passmanager.txt

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please provide info in all of the fields.")
    else:
        is_ok = messagebox.askokcancel(title='Confirm', message=f'This is what you entered: \nSite: {website}, '
                                                                f'\nUsername: {username}, \nPassword: {password}')
        if is_ok:
            # open the json file in read mode
            with open('passmanager.json', 'r') as passmanager:
                # load the file, save it in a variable
                data = json.load(passmanager)
                # update the data with new_data which is the dictionary with the new parameters
                data.update(new_data)
                # print(data)
                # so data is now updated, contains both the old dictionary and the new dictionary
                # store that data back into the json, but first open the file in write mode
            with open('passmanager.json', 'w') as passmanager:
                json.dump(data, passmanager, indent=4)
            site_entry.delete(0, tkinter.END)
            pass_entry.delete(0, tkinter.END)
            # (0, END) deletes all characters from the zeroth index till the END

# Okay so this is prone to fail, suppose the json file did not exist or did not have any data
# In those cases, the program will fail
# We want to add some try except block here


# 275 Challenge 1 - Handling Exceptions in the Password Manager

# So essentially what happens is if the passmanager.json file does not exist, it's not like the program will create one
# It will throw an error, and the program will crash

if is_ok:
    # try with the prescribed method first
    try:
        # something that might cause an exception
        with open('passmanager.json', 'r') as passmanager:
            data = json.load(passmanager)
            data.update(new_data)
    # if there is an error, then create a new json file and write the new_data into it
    except FileNotFoundError:
        # do this if there is an exception
        with open('passmanager.json', 'w') as passmanager:
            json.dump(new_data, passmanager, indent=4)
    else:
        # do this if there is not any exceptions
        with open('passmanager.json', 'w') as passmanager:
        # this is going to be triggered if no exceptions because json.dump takes data as an input
            json.dump(data, passmanager, indent=4)
    finally:
        # do this no matter what happens
        site_entry.delete(0, tkinter.END)
        pass_entry.delete(0, tkinter.END)


# 276 Challenge 2 - Search for a Website in the Password Manager

# 1. Add a search button (try putting it beside the Website entry first)
search = tkinter.Button(text="Search", font=('Courier', 10, 'bold'), bg=SCARLET, width=20)
search.grid(column=2, row=1)

# 2. Add a search function, where it takes the website entry, searches it against the keys, and responds with values
def lookup():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    import json
    with open('passmanager.json', 'r') as passmanager:
        data_dict = json.load(passmanager)
        print(data_dict)

# 3. Add a pop up, titled the website name, containing the username and pass
        if website in data_dict:
            messagebox.showinfo(title=website, message=f"Username: {data_dict[website]['username']}\n"
                                                     f"Password: {data_dict[website]['password']}")
            pyperclip.copy(data_dict[website]['password'])
        else:
            messagebox.showinfo(title="Error", message=f"No data for {website} found")

# 4. Add exception handling, so that when there is no json file to begin with, the pop will show error
try:
    with open('passmanager.json', 'r') as passmanager:
        data_dict = json.load(passmanager)
except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No data file found")
else:
    if website in data_dict:
        messagebox.showinfo(title=website, message=f"Username: {data_dict[website]['username']}\n"
                                                   f"Password: {data_dict[website]['password']}")
        pyperclip.copy(data_dict[website]['password'])
    else:
        messagebox.showinfo(title="Error", message=f"No data for {website} found")



# 5. Put it all together

import tkinter
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for i in range(1, nr_letters + 1)]
    pass_numbers = [random.choice(numbers) for j in range(1, nr_numbers+1)]
    pass_symbols = [random.choice(symbols) for k in range(1, nr_symbols+1)]
    pass_list = pass_letters + pass_numbers + pass_symbols

    random.shuffle(pass_list)
    final_pass = ''.join(pass_list)
    pass_entry.delete(0, tkinter.END)
    pass_entry.insert(0, final_pass)
    # we want to be able to have the newly generated password copied in the clipboard so we can paste it in the website
    pyperclip.copy(final_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_click():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    # create a new nested dictionary with website as key and username and pass as values
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # messagebox.showinfo(title="Success", message="Done")
    # instead of this, use the askokcancel method, it generates a boolean value if clicked ok/cancel
    # use that to record the info on the passmanager.txt

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please provide info in all of the fields.")
    else:
        is_ok = messagebox.askokcancel(title='Confirm', message=f'This is what you entered: \nSite: {website}, '
                                                                f'\nUsername: {username}, \nPassword: {password}')
        if is_ok:
            try:
                with open('passmanager.json', 'r') as passmanager:
                    data = json.load(passmanager)
                    data.update(new_data)
            except FileNotFoundError:
                with open('passmanager.json', 'w') as passmanager:
                    json.dump(new_data, passmanager, indent=4)
            else:
                with open('passmanager.json', 'w') as passmanager:
                    json.dump(data, passmanager, indent=4)
            finally:
                site_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)
                # (0, END) deletes all characters from the zeroth index till the END

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #


def lookup():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    try:
        with open('passmanager.json', 'r') as passmanager:
            data_dict = json.load(passmanager)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data_dict:
            messagebox.showinfo(title=website, message=f"Username: {data_dict[website]['username']}\n"
                                                     f"Password: {data_dict[website]['password']}")
            pyperclip.copy(data_dict[website]['password'])
        else:
            messagebox.showinfo(title="Error", message=f"No data for {website} found")


# ---------------------------- UI SETUP ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
SCARLET = "#5f5f5f"

# Window
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, )

# Canvas
canvas = tkinter.Canvas(width=200, height=200)
canvas.grid(column=1, row=0)

# Image
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)

# Label(s)
site_label = tkinter.Label(text='Website: ', font=('Courier', 10, 'bold'))
site_label.grid(column=0, row=1)
user_label = tkinter.Label(text='Email/Username: ', font=('Courier', 10, 'bold'))
user_label.grid(column=0, row=2)
pass_label = tkinter.Label(text='Password: ', font=('Courier', 10, 'bold'))
pass_label.grid(column=0, row=3)

# Entry(s)
site_entry = tkinter.Entry(width=40)
# use columnspan() here to stretch the widget across two cells
site_entry.grid(column=1, row=1)
# this makes the cursor start out in this box
site_entry.focus()

username_entry = tkinter.Entry(width=68)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(tkinter.END, "rough.rafi@gmail.com")

pass_entry = tkinter.Entry(width=40)
pass_entry.grid(column=1, row=3)

# Buttons
generator = tkinter.Button(text='Generate Password', font=('Courier', 10, 'bold'), width=20, bg=GREEN)
generator.config(command=generate_pass)
generator.grid(column=2, row=3)


add = tkinter.Button(text='Add', font=('Courier', 10, 'bold'), bg=YELLOW, width=20, command=add_click)
add.grid(column=2, row=4)


search = tkinter.Button(text="Search", font=('Courier', 10, 'bold'), bg=SCARLET, width=20)
search.config(command=lookup)
search.grid(column=2, row=1)


window.mainloop()
