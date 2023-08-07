import tkinter
from tkinter import messagebox
import pyperclip

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
