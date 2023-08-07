# 254 Day 28 Goals_ what we will make by the end of the day

# We will build a pomodoro application completely from scratch


# 255 How to work with the Canvas Widget and Add Images to Tkinter

# 1. Create the screen
from tkinter import *

screen = Tk()
screen.title('Pomodoro')

screen.mainloop()

# 2. Put the image of the tomato on the screen

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
# We will have to learn about the canvas widget
canvas = Canvas(width=1200, height=630)
# create an image object using the PhotoImage class. We cannot just give the image link here.
tomato_png = PhotoImage(file="tomato.png")
# place the canvas on the screen (denote x,y) with the image file
canvas.create_image(600, 315, image=tomato_png)
# lastly, pack the canvas to lay it out on the screen
canvas.pack()

screen.mainloop()

# image importing done

# 3. Resize the screen, so you can put other things in the screen later

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
# The image size is 690x362
canvas = Canvas(width=690, height=362)

tomato_png = PhotoImage(file="tomato-removebg-preview.png")
# We want the image to be at the center
canvas.create_image(345, 181, image=tomato_png)
# What if I add padding around the canvas?
canvas.pack(padx=100, pady=50)

screen.mainloop()

# Alternate method, we can add padding around the screen

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
# add padding to screen
screen.config(padx=100, pady=50)
# The image size is 690x362
canvas = Canvas(width=690, height=362)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
# We want the image to be at the center
canvas.create_image(345, 181, image=tomato_png)
# What if I add padding around the canvas?
canvas.pack()

screen.mainloop()

# 4. Add text to the screen

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
canvas = Canvas(width=690, height=362)

tomato_png = PhotoImage(file="tomato-removebg-preview.png")

canvas.create_image(345, 181, image=tomato_png)
# add text
canvas.create_text(345, 181, text="00:00")
canvas.pack(padx=100, pady=50)

screen.mainloop()

# Alternate method, add a label widget instead of create text

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
label = Label()
label.config(text='00:00', font=("Courier", 50, 'bold'))
canvas = Canvas(width=690, height=362)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
canvas.create_image(345, 181, image=tomato_png)
canvas.place(x=345, y=181)
label.place(x=200, y=200)
screen.mainloop()
# this way the label gets placed at the bottom
# if we want to position it over the image, we are going to have to use place() with x.y for all layout
# nope, does not work, the label goes behind the image
# so much for alternate methods

# 5. Change the text properties

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
canvas = Canvas(width=690, height=362)

tomato_png = PhotoImage(file="tomato-removebg-preview.png")

canvas.create_image(345, 181, image=tomato_png)
# modify text
canvas.create_text(345, 190, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.pack(padx=100, pady=50)

screen.mainloop()

# 6. Change background color

# add hex
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
from tkinter import *

screen = Tk()
screen.title('Pomodoro')
# change background color
screen.config(bg=GREEN)
# change background color of the canvas too, to get rid of the tomato pictures background
# also set highlightthickness=0 to get rid of the picture border
canvas = Canvas(width=690, height=362, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
canvas.create_image(345, 181, image=tomato_png)
canvas.create_text(345, 190, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.pack(padx=100, pady=50)

screen.mainloop()

# 256 Challenge - Complete the Application's User Interface (UI)

# 1. Put a timer at the top
# 2. Put a start button, place it at the lower left side of the tomato
# 3. Put a Reset button, place it at the lower right side
# 4 . Put a checkmark below the tomato

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
from tkinter import *

# Screen
screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

# 1. Put a timer label at the top, fg to change text color, bg to change the label background color
label = Label(text="Timer", fg='black', bg=GREEN, font=('Courier', 50, 'bold'))
label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=690, height=362, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
canvas.create_image(345, 181, image=tomato_png)
canvas.create_text(345, 190, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.grid(column=1, row=1, padx=100, pady=50)

# 2. Put a start button, place it at the lower left side of the tomato
start_button = Button(text='Start', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
start_button.grid(column=0, row=2)

# 3. Put a reset button, place it at the lower right side of the tomato
reset_button = Button(text='Reset', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
reset_button.grid(column=2, row=2)

# 4. Put a checkmark below the tomato
check_label = Label(text="🗸", fg='black', bg=GREEN, font=('Courier', 40, 'bold'))
check_label.grid(column=1, row=2)

screen.mainloop()

# 257 Add a Count Down Mechanism

# how does the time module work?
import time

for i in range(5):
    print(i)
    time.sleep(1)

# 0
# 1
# 2
# 3
# 4
# Now these get printed at one second intervals

# We could use the same principle in creating a timer
count = 1500
# 1500 secs for 25 min
import time

for i in range(1501):
    # so it loops through 1500 times
    # code for removing text on top of tomato
    time.sleep(1)


# However, this will not work in this case
# because this code above will generate output in the console
# whereas we are working with a GUI here, where the program keeps listening for any kind of user input
# like the button press and the subsequent changes
# it will have to keep checking if something happens, and the moment it does, it's got to react
# these types of programs are called "event driven"

# the way it keeps watching and listening is through the line mainloop()
# meaning it loops through the entire code every millisecond
# another loop in the program, and it will not even launch

# Luckily tkinter already thought of this
# use window.after(ms, func, arguments to pass in the function) method

screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

def say_something(thing):
    print(thing)

screen.after(1000, say_something, 'Hello')

screen.mainloop()

# The window gets printed and "Hello" gets printed after 1000 ms, or 1 sec

# Timestamp - 05:18

# This screen.after() is created with *args method and takes infinite positional arguments
from tkinter import *

screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

def say_something(thing, thang, thung, thong):
    print(thing)
    print(thang)
    print(thung)
    print(thong)

screen.after(1000, say_something, 'Hello', 'Hollo', 'Hullo', 'Hallo')

screen.mainloop()

# Hello
# Hollo
# Hullo
# Hallo
# These get printed after a delay of  1 sec

# Now how can we use this to loop for 5 sec? for 10 sec?

def count_down(sec):
    print(sec)
    if sec < 0:
        screen.after(1000, count_down, sec - 1)

# Now if we call this function what will happen?
# it will print "sec"
# then it will check if count is less than zero
# then it will call the screen.after() method
# inside the method, it will encounter the count_down function again
# at which point it will start again from step 1

from tkinter import *

screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

def count_down(sec):
    print(sec)
    if sec > 0:
        screen.after(1000, count_down, sec - 1)

count_down(10)
screen.mainloop()
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# printed at one second intervals, just like a loop

# How can we change the timer text instead of printing a countdown?

# Screen
screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

# Canvas
canvas = Canvas(width=690, height=362, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
canvas.create_image(345, 181, image=tomato_png)
timer_text = canvas.create_text(345, 190, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.grid(column=1, row=1, padx=100, pady=50)

def count_down(sec):
    # changing a text in the canvas is not the same as changing a label
    # in a label I would do label.config(), but here
    # canvas.itemconfig(which canvas, what element)
    # for convenience, store the canvas.create_text() in a variable
    canvas.itemconfig(timer_text, text=sec)
    if sec > 0:
        screen.after(1000, count_down, sec - 1)

# count_down(10)
# screen.mainloop()
# Nice, I can see a countdown

# How can we tie this with the start button press?
# Just configure the button so that when it gets pressed, the function gets executed

'''
# Button
start_button = Button(text='Start', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
start_button.config(command=count_down)
start_button.grid(column=0, row=2)

screen.mainloop()
'''
# does not work, because there is no way to specify the seconds
# what if I do this?

def start_timer():
    count_down(10)
# Button
start_button = Button(text='Start', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)
screen.mainloop()

# VOILA

# How to count down from 25 minutes?
sec = 1500
# How to display this second into a mm:ss format?
import math
timer_min = math.floor(sec / 60)
timer_sec = sec % 60

print(timer_min)
print(timer_sec)

# 25:0

# now make the changes in the timer text section, where you change the timer text every second

def count_down(sec):
    timer_min = math.floor(sec / 60)
    timer_sec = sec % 60
    canvas.itemconfig(timer_text, text=f'{timer_min}:{timer_sec}')
    if sec > 0:
        screen.after(1000, count_down, sec - 1)

# All good, it does a count down with proper mm:ss format
# But it shows 5:0 when it reaches five minutes
# how to make it show 05:00
# for that we need to understand dynamic typing


# 258 Dynamic Typing Explained

# What is dynamic typing?
# How could we address this problem where it does not show the preceding zero when the timer reaches one digit numbers?
# for seconds, we could do this
if timer_sec == 0:
    timer_sec = '00'
# now look here, we are changing a data type from integer to string
# this is called dynamic typing
# to apply this for both the minutes and seconds count
if timer_min < 10: #integer
    timer_min = f'{0}{math.floor(sec / 60)}' #string
if timer_sec < 10: #integer
    timer_sec = f'{0}{sec % 60}' #string
canvas.itemconfig(timer_text, text=f'{timer_min}:{timer_sec}')
# this is something unique to python, changing data types, just like that, remember that
# Python typing is Dynamic so you can change a string variable to an int (in a Static language you can't)
#
# x = 'somestring'
# x = 50
#
# Python typing is Strong so you can't merge types:
# 'foo' + 3 --> TypeError: cannot concatenate 'str' and 'int' objects
#
# In weakly-typed Javascript this happens...
# 'foo'+3 = 'foo3'


# 259 Setting Different Timer Sessions and Values

# In the pomodoro.py file, add
def start_timer():
    global reps
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(WORK_MIN*60)
        # I also want the title to say work
        label.config(text="WORK", fg=RED)
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(SHORT_BREAK_MIN*60)
        # I also want the title to say break
        label.config(text="BREAK", fg=YELLOW)
    elif reps == 7:
        count_down(LONG_BREAK_MIN*60)
        # I also want the title to say break
        label.config(text="BREAK", fg='black')
    reps += 1
# In the button section, add
start_button = Button(text='Start', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)

# finally in the count_down function, add (if you want to continue after one cycle is complete)
canvas.itemconfig(timer_text, text=f'{timer_min}:{timer_sec}')
if sec > 0:
    screen.after(1000, count_down, sec - 1)
# if you want to continue the timer once it completes a work cycle
# else:
#     start_timer()


# 260 Adding Checkmarks and Resetting the Application

# Adding checkmarks

check_mark = ''
# I also want a check mark to be generated once a work session is complete
    # this check mark should be generated after every work session is complete and a break session begins
    # so when reps == 1, 3, 5, 7
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(5)
        # I also want the title to say break
        label.config(text="BREAK", fg=YELLOW)
        check_mark = check_mark + '🗸'
        check_label.config(text=f'{check_mark}')
    elif reps == 7:
        count_down(20)
        # I also want the title to say break
        label.config(text="BREAK", fg='black')
        check_mark = check_mark + '🗸'
        check_label.config(text=f'{check_mark}')

# Reset function

timer = None

def count_down(sec):
    if sec > 0:
        global timer
        timer = screen.after(1000, count_down, sec - 1)
def reset_timer():
    screen.after_cancel(timer)
    # change timer text
    canvas.itemconfig(timer_text, text=f'00:00')
    # change label to 'timer'
    label.config(text="Timer", fg='black')
    # reset checkmarks
    global check_mark
    check_mark = ''
    check_label.config(text=f'{check_mark}')
    # once you hit reset and start again the reps will be 2 and it will start from a break, fix that
    global reps
    reps = 0

reset_button.config(command=reset_timer)

# Done


# Put everything together

from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer Mechanism
# 25 5 25 5 25 5 25 20
reps = 0
check_mark = ''
timer = None

# Timer reset


def reset_timer():
    screen.after_cancel(timer)
    # change timer text
    canvas.itemconfig(timer_text, text=f'00:00')
    # change label to 'timer'
    label.config(text="Timer", fg='black')
    # reset checkmarks
    global check_mark
    check_mark = ''
    check_label.config(text=f'{check_mark}')
    # once you hit reset and start again the reps will be 2 and it will start from a break, fix that
    global reps
    reps = 0

def start_timer():
    global reps
    global check_mark
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(10)
        # I also want the title to say work
        label.config(text="WORK", fg=RED)
    # I also want a check mark to be generated once a work session is complete
    # this check mark should be generated after every work session is complete and a break session begins
    # so when reps == 1, 3, 5, 7
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(5)
        # I also want the title to say break
        label.config(text="BREAK", fg=YELLOW)
        check_mark = check_mark + '🗸'
        check_label.config(text=f'{check_mark}')
    elif reps == 7:
        count_down(20)
        # I also want the title to say break
        label.config(text="BREAK", fg='black')
        check_mark = check_mark + '🗸'
        check_label.config(text=f'{check_mark}')
    reps += 1


# Countdown Mechanism


def count_down(sec):
    timer_min = math.floor(sec / 60)
    timer_sec = sec % 60
    # if timer_sec == 0:
    #     timer_sec = '00'
    if timer_min < 10:
        timer_min = f'{0}{math.floor(sec / 60)}'
    if timer_sec < 10:
        timer_sec = f'{0}{sec % 60}'
    canvas.itemconfig(timer_text, text=f'{timer_min}:{timer_sec}')
    if sec > 0:
        global timer
        timer = screen.after(1000, count_down, sec - 1)
    # if you want to continue the timer once it completes a work cycle
    # else:
    #     start_timer()


# UI Setup

# Screen
screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

# 1. Put a timer label at the top, fg to change text color, bg to change the label background color
label = Label(text="Timer", fg='black', bg=GREEN, font=('Courier', 50, 'bold'))
label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=690, height=362, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
canvas.create_image(345, 181, image=tomato_png)
timer_text = canvas.create_text(345, 190, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.grid(column=1, row=1, padx=100, pady=50)

# 2. Put a start button, place it at the lower left side of the tomato
start_button = Button(text='Start', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)


# 3. Put a reset button, place it at the lower right side of the tomato
reset_button = Button(text='Reset', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=2)

# 4. Put a checkmark below the tomato
check_label = Label(text="", fg='black', bg=GREEN, font=('Courier', 40, 'bold'))
check_label.grid(column=1, row=2)

screen.mainloop()
