# 261 Day 29 Goals_ what we will make by the end of the day

# By the end of the day we will have built a password manager

# Will have the following fields -
# Website Name
# Email
# Password
# Generate Password
# Add(Data will be added to a text file)


# 262 Challenge 1 - Working with Images and Setting up the Canvas

# Create a window using tkinter with the title password
# The window will only contain a canvas widget
# The canvas width and height will be 200 pixels
# The canvas will be padded on the edges by 20 pixels
# The image will be at the center of the canvas

# Window
import tkinter
window = tkinter.Tk()
window.title('Password Manager')

# Canvas
canvas = tkinter.Canvas(width=600, height=600)
canvas.grid(padx=20, pady=20, column=1, row=1)
# Image
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(300, 300, image=logo)


window.mainloop()


# 263 Challenge 2 - Use grid() and columnspan to Complete the User Interface

# what if we want one particular widget to span through 2 columns?
# that is where we use columnspan
# use columnspan = 2 inside the grid method, as an argument to get the desired result

# Label(s)
site_label = tkinter.Label(text='Website: ', font=('Courier', 10, 'bold'))
site_label.grid(column=0, row=1)
user_label = tkinter.Label(text='Email/Username: ', font=('Courier', 10, 'bold'))
user_label.grid(column=0, row=2)
pass_label = tkinter.Label(text='Password: ', font=('Courier', 10, 'bold'))
pass_label.grid(column=0, row=3)

# Entry(s)
site_entry = tkinter.Entry(width=35)
# use columnspan() here to stretch the widget across two cells
site_entry.grid(column=1, row=1, columnspan=3)


username_entry = tkinter.Entry(width=21)
username_entry.grid(column=1, row=2)

pass_entry = tkinter.Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
generator = tkinter.Button(text='Generate Password', font=('Courier', 10, 'bold'), width=36)
generator.grid(column=2, row=3)

add = tkinter.Button(text='Add', font=('Courier', 10, 'bold'), width=36)
add.grid(column=1, row=4)


# 264 Solution to the Creating the Grid Layout

# Slight design changes

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Window
import tkinter
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50,)

# Canvas
canvas = tkinter.Canvas(width=200, height=200)
canvas.grid(column=1, row=0)

#Image
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
site_entry = tkinter.Entry(width=80)
# use columnspan() here to stretch the widget across two cells
site_entry.grid(column=1, row=1, columnspan=2)


username_entry = tkinter.Entry(width=80)
username_entry.grid(column=1, row=2, columnspan=2)

pass_entry = tkinter.Entry(width=80)
pass_entry.grid(column=1, row=3, columnspan=2)

# Buttons
generator = tkinter.Button(text='Generate Password', font=('Courier', 10, 'bold'), width=25, bg=GREEN)
generator.grid(column=1, row=4)

add = tkinter.Button(text='Add', font=('Courier', 10, 'bold'), bg=YELLOW)
add.grid(column=1, row=5, columnspan=2)

window.mainloop()


# 265 Challenge 3 - Saving Data to File

# to keep the cursor at the site entry box -
site_entry.focus()

# if you want your email/username entry to be pre populated with your most commonly used email, i.e. rough.rafi
# username_entry.insert(index= , string= )
# index can take one of two values, 0 or END, 0 means the cursor will be at the start of the text, END means otherwise
# string is a string
username_entry.insert(tkinter.END, "rough.rafi@gmail.com")

# challenge
# take the entry texts and store them in a variable
# once the add button is pressed, the data will be stored in a file and the website and password field will clear

# in the password_manager.py file, add -

def add_click():
    website = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
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
        # (0, END) deletes all characters from the zeroth index till the END

# Also, add button command

add = tkinter.Button(text='Add', font=('Courier', 10, 'bold'), bg=YELLOW, width=25, command=add_click)

# Done


# 266 Dialog Boxes and Pop-Ups in Tkinter

# Standard Dialogues in tkinter
# These are basically pop ups that you can generate in tkinter

# One of the standard dialogues in message boxes
# You have to import message boxes even if you have declared from tkinter import *
# Because this message box is not actually a class

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
            # (0, END) deletes all characters from the zeroth index till the END


# 267 Generate a Password & Copy it to the Clipboard

# Remember the password geenrator project from day 5?
# We are going to copy it here
# But we are going to modify the code there first because now we know things we did not know then, so we can optimize

# in the pass_generator_from_day5.py file -
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Slight modification, so it does not need any input
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# for i in range(1, nr_letters+1):
#     password = password + ' ' + random.choice(letters)
# for j in range(1, nr_numbers+1):
#     password = password + ' ' + random.choice(numbers)
# for k in range(1, nr_symbols+1):
#     password = password + ' ' + random.choice(symbols)

# Use list comprehension here instead to bypass these for loops above

pass_letters = [random.choice(letters) for i in range(1, nr_letters + 1)]
pass_numbers = [random.choice(numbers) for j in range(1, nr_numbers+1)]
pass_symbols = [random.choice(symbols) for k in range(1, nr_symbols+1)]
# initially we had a password string which we converted to a list, we will get the list directly now
pass_list = pass_letters + pass_numbers + pass_symbols
random.shuffle(pass_list)
# final_pass = ''
# for m in pass_list:
#     final_pass += m
# use join() here instead
final_pass = ''.join(pass_list)
print(final_pass)

# now in the password_manager.py file -
# in the password generator section -

def def generate_pass():
    # all the code above
    # instead of print(final_pass), do this
    pass_entry.delete(0, tkinter.END) #delete the previously generated pass, from 0 to END
    pass_entry.insert(0, final_pass) #insert the newly generated final_pass, from 0
    # we want to be able to have the newly generated password copied in the clipboard, so we can paste it in the website
    # install and import pyperclip
    pyperclip.copy(final_pass)

# in the generator button -
generator.config(command=generate_pass)

# Done, finally



# Put it all together

import tkinter
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
                # (0, END) deletes all characters from the zeroth index till the END


# ---------------------------- UI SETUP ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

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
site_entry = tkinter.Entry(width=80)
# use columnspan() here to stretch the widget across two cells
site_entry.grid(column=1, row=1, columnspan=2)
# this makes the cursor start out in this box
site_entry.focus()

username_entry = tkinter.Entry(width=80)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(tkinter.END, "rough.rafi@gmail.com")

pass_entry = tkinter.Entry(width=80)
pass_entry.grid(column=1, row=3, columnspan=2)

# Buttons
generator = tkinter.Button(text='Generate Password', font=('Courier', 10, 'bold'), width=25, bg=GREEN)
generator.config(command=generate_pass)
generator.grid(column=1, row=4)


add = tkinter.Button(text='Add', font=('Courier', 10, 'bold'), bg=YELLOW, width=25, command=add_click)
add.grid(column=1, row=5)

window.mainloop()
