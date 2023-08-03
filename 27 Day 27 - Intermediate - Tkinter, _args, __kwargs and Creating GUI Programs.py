# 244 Day 27 Goals_ what we will make by the end of the day

# We will be diving into GUIs using Tkinter
# We will be creating forms, with labels, buttons and inputs

# We will also look into some advanced features of python functions
# Including default arguments, args and kwargs
# So a way of being able to pass and undefined amount of inputs into a function

# We will build a unit converter - miles to km, l to gallons etc.


# 245 History of GUI and Introduction to Tkinter

# We basically use Tkinter to create GUIs
# GUIs were a huge deal back in the 90s,
# because back in those days the only way one could interact with a computer was MS-DOs
#
# GUI came and changed that
# GUIs were graphical and could be interacted with a mouse

# Initially Apple invented GUIs, in the computer Mac Lisa
# Then Microsoft came up with their own version, called Windows
# Everyone started becoming skeptical about Windows being a genuine IP of Microsoft
# Then later it was found out that even Apple had stolen the idea from Xerox PARC
# Xerox PARC was a research center that was, at that time, creating loads of breakthrough in the world of computing


# 246 Creating Windows and Labels with Tkinter

# Tkinter, like Turtle is already preinstalled in python

import tkinter

# This is how we create a new window
from tkinter import END

window = tkinter.Tk()
# But when we run it nothing happens
# We need to keep the window on the screen

# we could create a while loop, something like this -
# while True:
#     listen
# this loop is available in the module in the form of -
window.mainloop()
# now when we run it, we can see a blank window
# tkinter keeps the window on the screen, listening for inputs such as mouse clicks on keyboard presses

# just like screen.exitonclick() in turtle, this window.mainloop() should also be at the end of your program

# So starting afresh I am going to keep the windows.mainloop() at the bottom of our code

# giving your window a title
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')

window.mainloop()
# we can see that the window now has a title()

# change the size of the window
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

window.mainloop()
# we can see that the window size has changed to the dimension we gave

# now we can add components to our window, first let's create a label
# creating a label
# we have to tap into the label class and create a label object, just like we created a window object
my_label = tkinter.Label(text='I am a label')
# just adding this line will not work, we will need to specify how our label would be laid out in the window
# when it comes to laying out any components, we need to call the pack() method

# So now, creating a label and showing it on the screen
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label')
my_label.pack()

window.mainloop()
# now we can see the window with the label at the center

# changing the style of the label
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Arial", 24, 'bold', 'italic'))
# if you do not want italic, just leave out that part
my_label.pack()

window.mainloop()
# the font size and style has changed in the window

# Reminder = none of your components would show up unless you use the packer, i.e. pack()

# the pack() method can take a few arguments, let's explore
# 1.
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Arial", 24, 'bold', 'italic'))
# if you do not want italic, just leave out that part
my_label.pack(side='left')

window.mainloop()
# the label is now at the left

# 2.
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Arial", 24, 'bold', 'italic'))
# if you do not want italic, just leave out that part
my_label.pack(side='left', expand=True)

window.mainloop()
# the label gets expanded, to the center

# when we hover our mouse in the parenthesis, we do not get a direction as to how many and what arguments it can take
# turtle methods on the other hand had specific instructions
import turtle
tim = turtle.Turtle()
tim.write()
# when we hover the mouse inside the parenthesis in write, we get to see options like, font, text etc.
# in pack() we do not, however we know that we can put a number of arguments inside as per the documentation

# what is going on here?


# 247 Setting Default Values for Optional Arguments inside a Function Header

# Advanced Python Arguments

# keyword arguments -
def my_function(a, b, c):
    return a+b+c
my_function(1, 2, 3)

# what if we already know what a, b and c are gonna be? what if we want to set a default value to them?
# default arguments -
def my_function(a=1, b=2, c=3):
    return a+b+c
my_function()

# and when we want to change the argument value inside the function?
def my_function(a=1, b=2, c=3):
    return a+b+c
my_function(a=5)

# getting to the previous example
import turtle
tim = turtle.Turtle()
tim.write()
# you know that we do not have to provide all the arguments, we could just provide one or two
# it will still work because all the arguments already have a default value
# if you do not provide anything the method is going to conform to the default value
# we have to provide the required arguments though, which is the first arg or the text it is expecting to write


# 248 _args_ Many Positional Arguments

def add(n1, n2):
    return n1+n2


print(add(4,5))
# 9

# what if i want the function to be able to take unlimited values, for addition?
def add(*args):
    for n in args:
        # do this

# challenge - write the code such that you can add any number of inputs to the add() and it will return the summationo
def add(*args):
    summation = 0
    for n in args:
        summation += n
    return summation

print(add(1,2,3,4))
# 10
print(add(1,2,3,4,5,6,7,8,9,10))
# 55

# since we can loop through, we can also use indexing?
def add(*args):
    summation = 0
    for n in args[1:3]:
        summation += n
    return summation

print(add(1,2,3,4,5,6,7,8,9))
# it should add 2,3
# 5

# Yes!

# These are thus called unlimited positional arguments, because positioning is imp since you are using indexing

# but waht if i want to refer to my arguments by name?
# text, size, font, aligh etc.
# how will i incorporate unlimited arguments then?


# 249 __kwargs_ Many Keyword Arguments

# double asterix operator (**)

# the single asterix operator generates a tuple, and we use indexing or loops to do things with them
def add(*args):
    print(args)
print(add(1,2,3,4,5,6,7,8,9))
# (1, 2, 3, 4, 5, 6, 7, 8, 9)

# the double asterix generator on the other hand generates a dictionary
def calculate(**kwargs):
    print(kwargs)
print(calculate(add=5, multiply=6))
# {'add': 5, 'multiply': 6}
# we can use this dictionary to do things we want

# example -
def calculate(n, **kwargs):
    # at this point, it creates a blank dict like this -
    # {"": "", "": ""}
    # when we add the keys and the values when calling the function, the dict gets created
    # and then we tell beforehand what to do with the keys and values to be received later
    n += kwargs['add']
    n *= kwargs['multiply']
    return n
print(calculate(10, add=5, multiply=6))
# this should essentially return 10+5*6
# 90

# now with this same principle explain the tkinter module
# we saw that when we called pack() module, no arguments were asked for
# so when we called the pack() module a dictionary was created with all the 'keys'
# in the class -
# def pack():
    # {
    #     "text": "",
    #     "align": "",
    #     "font": "",
    #     ...
    #  }

    # print(text)

# and when we call on the method -
# object.pack(text = 'this is dope')
# it creates the value for the key 'text'
# and prints it

# the tkinter module is created using another module named Tk
# now TK has a very similar purpose but very different syntax from python
# so all the tk methods were imported to tkinter but with python syntax
# and this wad the most efficient way for them to do this
# thus we do not have argument suggestions when we call a method, like pack()

# can we create a class like this?
# yeah

# without kwargs
class Person:
    def __init__(self, name, wife):
        self.nametag = name
        self.spouse = wife

rafi = Person("Rafi", "Teetly")
numayer = Person("Numayer", "Amy")
print(rafi.nametag)
print(rafi.spouse)
print(numayer.nametag)
print(numayer.spouse)
# Rafi
# Teetly
# Numayer
# Amy

# with kwargs
class Person:
    def __init__(self, **kw):
        # this initialization creates the dict, now with empty keys and values
        self.nametag = kw['name']
        self.spouse = kw['wife']
        # this delineates the arguments that the object might have, i.e. keys in the dict, but values are still empty

rafi = Person(name= "Rafi", wife= "Teetly")
numayer = Person(name="Numayer", wife= "Amy")
print(rafi.nametag)
print(rafi.spouse)
print(numayer.nametag)
print(numayer.spouse)
# Rafi
# Teetly
# Numayer
# Amy

# in case you used **kw while creating a class and forgot to specify one of the arguments,
# i.e. one of the keys in the dict
# it will not work

class Person:
    def __init__(self, **kw):
        # self.nametag = kw['name'], comment out this key
        self.spouse = kw['wife']
        # this means that the dict now has only one key, wife

rafi = Person(name= "Rafi", wife= "Teetly")
print(rafi.nametag)
print(rafi.spouse)
# AttributeError: 'Person' object has no attribute 'nametag'

# what if i did not specify an argument while creating the object?

class Person:
    def __init__(self, **kw):
        # this initialization creates the dict, now with empty keys and values
        self.nametag = kw['name']
        self.spouse = kw['wife']
        # this delineates the arguments that the object might have, i.e. keys in the dict, but values are still empty

rafi = Person(name= "Rafi")
print(rafi.nametag)
print(rafi.spouse)
# KeyError: 'wife'

# to bypass this, like in pack(), where we specified only the text but not the font or the size
# it did not give us an error then

# from the autbor notes -
#The get() dictionary method
#This helps as a get around for KeyError messages
#What if I want to find a key from a dict, but not sure if the key exists at all
#Also I don't want the KeyError to mess my code

#Let's say I want hair from myWife, but don't want the crash if it doesn't exist

print(myWife.get('hair', 0)) #if myWife contains 'hair', print it,else print 0
#0

class Person:
    def __init__(self, **kw):
        self.nametag = kw.get('name')
        self.spouse = kw.get('wife')
        self.color = kw.get('color')
        self.seats = kw.get('seats')
        # this delineates the arguments that the object might have, i.e. keys in the dict, but values are still empty
        # returns None if an argument is not provided

rafi = Person(name= "Rafi")
print(rafi.nametag)
print(rafi.spouse)
# Rafi
# None
# None
# None

# Quiz -
def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)
# What is the output of the code above?
# Answer - 4 (7, 3, 0) {'x': 10, 'y': 64}


# 250 Buttons, Entry, and Setting Component Options

# Changing Label Text
# this can be done in any of three ways
my_label.config(text = 'New Text')
my_label = tkinter.Label(text='New Text')
my_label['text'] = 'New Text'


import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Arial", 24, 'bold', 'italic'))
# if you do not want italic, just leave out that part
my_label.pack(side='left', expand=True)
my_label['text'] = 'New Text'

window.mainloop()
# we can see that the window now has a 'New Text' label

# Creating Buttons

import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
# my_label.pack(side='left', expand=True)
# commenting this out since i do not want my label to be left aligned
my_label['text'] = 'New Text'
# ***
button = tkinter.Button(text='Click Me', font="Courier")
# to make it visible, call on the pack method
button.pack()
# ***
window.mainloop()
# we can see that a new button has been created at the top corner of the window

# Assigning an action to the buttons

# first define a function that specifies what the button clicking does
def button_clicked():
    print('button clicked')
# Now change the button initialization with the optional argument command
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
# my_label.pack(side='left', expand=True)
# commenting this out since i do not want my label to be left aligned
my_label['text'] = 'New Text'
# ***
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
# to make it visible, call on the pack method
button.pack()
# ***
window.mainloop()
# we can see the click the button prints the text in the console

# challenge - button click should change the label text to 'button click'
n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')

import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
# my_label.pack(side='left', expand=True)
# commenting this out since i do not want my label to be left aligned
my_label['text'] = 'New Text'
# ***
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
# to make it visible, call on the pack method
button.pack()
# ***
window.mainloop()
# we can see every time we click the button it changes the text into "Button click + number"
# neat

# man the tkinter module has lots of classes, the pack() class with its own methods, label, button etc.

# Creating entries
# entries are text boxes where the users can type in their input

n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')

import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
my_label['text'] = 'New Text'
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
# to make it visible, call on the pack method
button.pack()
# ***
user_input = tkinter.Entry(width=20)
user_input.pack()
# ***
window.mainloop()
# we can see that a text box for user inputs has appeared
# now go back and change the width of that text box

# Get hold of the value from the entry
# use the get() method
# challenge - change the label into whatever is in user_input whenever button gets clicked


def button_clicked():
    # ***
    my_label.config(text= user_input.get())
    # ***

import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
my_label['text'] = 'New Text'
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.pack()
user_input = tkinter.Entry(width=20)
user_input.pack()

window.mainloop()


# 251 Other Tkinter Widgets_ Radiobuttons, Scales, Checkbuttons and more
# 1. in the existing code, add a starting line in the user_input field
# 2. create a text box, add a starting text
# 3. Get the input from the text box

def button_clicked():
    my_label.config(text= user_input.get())

import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
my_label['text'] = 'New Text'
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.pack()
user_input = tkinter.Entry(width=20)
user_input.pack()
# ***
# 1.
user_input.insert(tkinter.END, string="Type here")
# END is the index. END refers to the position after the existing text.
# END reside in the tkinter namespace, thus needs to be imported by tkinter.END
# 2.
text = tkinter.Text(height=5, width=30)
text.focus()
# this makes the cursor start out in this box
text.pack()
text.insert(tkinter.END, "Example of a multi line text entry")
# 3.
print(text.get("1.0", tkinter.END))
# 1.0 gets hold of the text starting from the first line at character 0
# ***

window.mainloop()


# 4. Create a spinbox
# 5. Get the value from the spinbox
# 6. create a scale
# 7. create a checkbox/button
# 8. create a radio button
# 9. create a list box

def button_clicked():
    my_label.config(text= user_input.get())

import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label.pack()
my_label['text'] = 'New Text'
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.pack()
user_input = tkinter.Entry(width=20)
user_input.pack()
user_input.insert(tkinter.END, string="Type here")
text = tkinter.Text(height=5, width=40)
text.focus()
text.pack()
text.insert(tkinter.END, "Example of a multi line text entry")
print(text.get("1.0", tkinter.END))


#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
print(scale.get())
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
# A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it
# as well using getter and setter methods. These variables can be passed to various widget parameters,
# for example, the variable parameter of Radio Button and CheckBox Button
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
# we can see a new spinbox has been created and everytime a value is changed it gets printed out in the console
# we can see a new scale has been created and everytime a value is changed it gets printed out in the console
# we can see a new checkbutton has been created and when checked the corresponding value gets printed out in the console
# we can see a new radiobutton has been created and when checked the corresponding value gets printed out in the console
# we can see a new listbox has been created and when selected the selection gets printed out in the console

# the above code is not very python-like because, as discussed earlier, the entire tkinter library has been
# imported from the tk module, which was initialliy meant for some other language, and given the vastness of tkinter,
# creating optional arguments and keyword arguments was the most efficient way for developers to properly transfer
# all functionalities to python


# 252 Tkinter Layout Managers_ pack(), place() and grid()

# coming back to the initial few lines of code -

n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')
# window
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
# label
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label['text'] = 'New Text'
my_label.pack()
# button
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.pack()
# entry
user_input = tkinter.Entry(width=20)
user_input.pack()

window.mainloop()

# tkinter essentially has three layout managers, using which we place/arrange the elements/widgets on the screen
# place(), place() and grid()
# packs() the widgets next to each other in a vaguely logical format
# pack() will start at the top and arrange each of the widgets one by one coming down
# we use arguments like side='left'/'bottom'/etc. to position the widgets using pack()
# the problem with pack() is that it is difficult to specify the exact position of a widget
# if i want widget A slightly higher than widget B, then it is a hassle doing it with pack()
# N.B, - if you create a widget but don't specify its layout using either pack(), place() or grid(), it won't be shown
place()
# place() is all about precise positioning

n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')
# window
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
# label
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label['text'] = 'New Text'
my_label.place(x=250, y=0)
# button
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.place(x=0, y=0)
# entry
user_input = tkinter.Entry(width=20)
user_input.place(x=250, y=150)

window.mainloop()

# the downside of place() is that it requires such precies metrics, that if you have a lot of widgets
# it becomes difficult to manage

grid()
# this imagines your entire window as a grid and places the widgets at specified grid

n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')
# window
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
# label
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label['text'] = 'New Text'
my_label.grid(column=0, row=0)
# now how does grid() know how many columns and rows there are in the window?
# it does not, it imagines that (column=0, row=0) is the top left corner of the window
# and for subsequent grid positions of other widgets, it places those relative to other widgets' positions
# button
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.grid(column=10, row=10)
# entry
user_input = tkinter.Entry(width=20)
user_input.grid(column=5, row=5)

window.mainloop()
# we can see that the three widgets have been placed diagonally

# N.B. You cannot mix up grid(), pack() in the same program

# challenge - in the existing program add another button, use grid() to position them like so -
# label.grid(column=0, row=0)
# new_button.grid(column=2, row=0)
# button.grid(column=1, row=1)
# user_input.grid(column=3, row=2)

n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')
# window
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
# label
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label['text'] = 'New Text'
my_label.grid(column=0, row=0)
# button
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.grid(column=1, row=1)
# new button
new_button = tkinter.Button(text='Click Me (New)', font="Courier", command=button_clicked)
new_button.grid(column=2, row=0)
# entry
user_input = tkinter.Entry(width=20)
user_input.grid(column=3, row=2)

window.mainloop()

# Adding padding around the components
# .config(padx=##, pady=##)

# add padding around the window and the user_input widget
n = 0
def button_clicked():
    global n
    n += 1
    my_label.config(text= f'Button Click {n}')
# window
import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)
# label
my_label = tkinter.Label(text='I am a label', font=("Courier", 24, 'bold'))
my_label['text'] = 'New Text'
my_label.grid(column=0, row=0)
# button
button = tkinter.Button(text='Click Me', font="Courier", command=button_clicked)
button.grid(column=1, row=1)
# new button
new_button = tkinter.Button(text='Click Me (New)', font="Courier", command=button_clicked)
new_button.grid(column=2, row=0)
new_button.config(padx=50, pady=50)
# entry
user_input = tkinter.Entry(width=20)
user_input.grid(column=3, row=2)
# user_input.config(padx=50, pady=50)
# padx and pady do not seem to be working on the entry widgets

window.mainloop()


# 253 Mile to Kilometers Converter Project

# 1. text entry for miles
# 2. label - Miles
# 3. label - is equal to
# 4. label - ##
# 5. label - Km
# 6. button - calculate


# 0. create window
window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(pady=20, padx=20)

# 1. text entry for miles
user_input = tkinter.Entry(width=15, justify='center', font=("Courier", 10, 'bold'))
user_input.grid(column=1, row=0)

# 2. label - Miles
miles = tkinter.Label(text='Miles', font=("Courier", 10, 'bold'))
miles.grid(column=2, row=0)

# 3. label - is equal to
equals = tkinter.Label(text='is equal to', font=("Courier", 10, 'bold'))
equals.grid(column=0, row=1)

# 4. label - ##
converted_num = tkinter.Label(text=" ", font=("Courier", 10, 'bold'))
converted_num.grid(column=1, row=1)

# 5. label - Km
km = tkinter.Label(text='Km', font=("Courier", 10, 'bold'))
km.grid(column=2, row=1)

# 6. button - calculate


def button_click():
    kms = 1.609344 * float(user_input.get())
    converted_num.config(text=f"{kms}")


button = tkinter.Button(text='Convert', font=("Courier", 10, 'bold'), command=button_click)
button.grid(column=1, row=2)

window.mainloop()

