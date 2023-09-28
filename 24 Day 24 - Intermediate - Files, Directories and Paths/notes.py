# 217 Day 24 Goals_ what you will make by the end of the day

# We will learn about local files and directories
#
# By the end of the day, we will have improved upon oir snake game, where we will have a high score beside player score
#
# We will also create a mail merge system, where we can personalize parts of our mail
# For example, Dear [Name]
# Imagine Akhteruddin Mahmood Bhai sending out 10000 personalized emails about PA rating
# He does not actually do it manually, typing 10,000 letters. Instead he uses a mail merge system
#
# And today we will learn how to create one


# 218 Add a High Score to the Snake Game

# in the scoreboard.py file add -
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(220, 280)
        self.write(f"Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(220, 280)
        self.write(f"Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.refresh()
        self.home()
        self.pendown()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

# in the snake_game.py file, add -
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        points.score += 1
        food.refresh()
        points.refresh()
        snake.increase_length()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        points.game_over()

    for i in snake.turtles[1:]:
        if snake.head.distance(i) < 10:
            game_on = False
            points.game_over()

# but we encounter a fatal flaw when we exit the game, the self.high_score re-initializes when we start the game
# and resets to 0
# so the highscore does not show the all time high score anymore, for the user to pursue
# what if we could store the highscore in a file, and during initialization set self.high_score to pull it from there?


# 219 How to Open, Read, and Write to Files using the _with_ Keyword

# Create a new text file under the project (Project > New > File > (type)my_file.txt)
# Open the .txt file in a new window
# Write Hello, Rafi here, in the file

# Remember the open() function from Automate the Boring Stuff with Python
# Since it creates a file object better to store it in a file
import os
print(os.getcwd())
# G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths

file = open(r'G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths\my_file.txt')
# OR, since it is in the target directory -
file = open(r'my_file.txt')
print(file.read())
# Hello, Rafi here

# Once done, close the file
file.close()
# Why do we need to close the file
# Because if it stays open, it consumes some memory, you close it to free up the memory

# But often times developers forget to close the file, since we are doing lots of actions with the file
# so they open the file a bit differently
with open(r'my_file.txt') as file:
    print(file.read())
# Hello, Rafi here

# the with keyword manages the file directly and as soon as it notices that you are done with it, it closes the file

# what if we want to write to it?
with open('my_file.txt') as file:
    file.write('I am 70 inches tall, give or take')
    # N.B. this is not append, this is write
    print(file.read())
# io.UnsupportedOperation: not writable
# this is because by default the file is opened as 'read only' mode

# for this to work, you need to open the file in write mode

with open('my_file.txt', mode='w') as file:
    file.write('I am 70 inches tall, give or take')
# you can see that in the my_file.txt file the text got changed

# Append
with open('my_file.txt', mode='a') as file:
    file.write('Nice to meet you')
    # appends adds to the file
# The my_file.txt now contains
# I am 70 inches tall, give or takeNice to meet you

# WHEN YOU OPEN A FILE IN WRITE MODE, AND THE FILE DOES NOT EXIST, THEN IT WILL ACTUALLY CREATE THE FILE FOR YOU
with open('new_file.txt', mode='w') as file:
    file.write('Nice to meet you')
# You can see that a new file has been created with the text - 'Nice to meet you'
# REMEMBER, THIS ONLY WORKS IN THE WRITE AND IF THE FILE DOES NOT CURRENTLY EXIST

# Now let's get back to the snake game


# 220 Challenge_ Read and Write the High Score to a File in Snake

# Create a new file called data.txt in the project folder, write 0 there as an initial value

# in the scoreboard.py file, make the changes -

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')
# this way if I want to change font I do not have to do it numerous times in code body


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as datafile:
            self.high_score = int(datafile.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(220, 280)
        self.write(f"Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(220, 280)
        self.write(f"Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as datafile:
                datafile.write(f"{self.score}")
        self.refresh()
        self.home()
        self.pendown()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

# that's it, everything else remains the same and everytime the game reboots the highscore is pulled from the data file


# 221 Understand Relative and Absolute File Paths

# The root folder, the absolute origin of the destination path, is denoted by a single forward slash
# /

# on windows computers, it is usually our C:\ Drive
# the file/folder is a way for the computer to navigate to the destination of interest

# G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths\notes.py
# this above is the absolute file path
# absolute file paths always start off relative to the root
# they always start from the origin, the root of the storage system

# ./notes.py
# file paths relative to the current working directory (cwd) are known as relative file paths

# Timestamp - 04:45

# the ./ signifies look in the current folder for this item
# ./notes.py
# if we switch our working directory to G:\Notes - 100 Days of Code, how do we get to the notes.py file?
# the absolute file path will remain the same
# however the relative file path will change to .\24 Day 24 - Intermediate - Files, Directories and Paths\notes.py

# how do we go back? let's say our cwd is \24 Day 24 - Intermediate - Files, Directories and Paths
# how to we move back one folder and select a file from \Notes - 100 Days of Code?
# ..\01 Day 1 - Beginner - Working with Variables in Python to Manage Data.py
# two dots represent going one step up in the hierarchy

# but if our cwd is \24 Day 24 - Intermediate - Files, Directories and Paths\ and we want to get hold of food.py?
# .\food.py
# we could just as well use food.py to get the file, since it is in the cwd

# challenge
# remember the code a few lines back
with open('my_file.txt') as file:
    file.write('I am 70 inches tall, give or take')
# you were able to use just the file name as the argument in the open function because the file awas in the cwd

# what if it was in the desktop?
with open(r'C:\Users\DELL\Desktop\my_file.txt') as file:
    # use raw text string when using backslash
    file.write('I am 70 inches tall, give or take')
# OR
with open('C:/Users/DELL/Desktop/my_file.txt') as file:
    # no need to use raw text string when using forward slash
    file.write('I am 70 inches tall, give or take')

# OR use os.path.join to get the file path in the "operating system compatible" format
import os
path = os.path.join('C', 'Users', 'DELL', "Desktop", 'my_file.txt')
print(path)
# C\Users\DELL\Desktop\my_file.txt

# One of the peculiarities between windows and Mac is that on a Mac the separator is / and on Windows it is \

# challenge
# do the above exercise but in terms of relative file path
# put a copy of my_file.txt in the G: Drive
# so currently the cwd is G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths
# move back, go to G, find file and all that -  how do you do it relative to the cwd?

# Remember - two dots represent going one step up in the hierarchy

import os
print(os.getcwd())
# G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths
with open(r'..\..\my_file.txt') as file:
    # move back two times
    print(file.read())
# I am 70 inches tall, give or takeNice to meet you

# the absolute file path is relative to your root folder, your drives
# the relative file path is relative to your cwd


# 222 Introducing the Mail Merge Challenge

# Tasks
# 1. Get hold of the sample letter text
# open the main.py in the "Mail merge project start folder"
with open(r'G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths\Mail Merge Project '
          r'Start\Input\Letters\starting_letter.txt') as file:
    mail_text = file.read()
    print(mail_text)
# Dear [name],
# You are invited to my birthday this Saturday.
# Hope you can make it!

# 2. Get hold of the names
with open(r'G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths'
          r'\Mail Merge Project Start\Input\Names\invited_names.txt') as file:
    names_list = file.readlines()
    print(names_list)
# ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']
# not quite the way I want
for i in names_list:
    print(i.strip('\n'))
# Aang
# Zuko
# Appa
# Katara
# Sokka
# Momo
# Uncle Iroh
# Toph

# so yeah, should not be a problem, will work out later

# 3. Replace the [name] in the sample letter with the names gathered from step 2

for i in names_list:
    new_mail_text = mail_text.replace('[name]', i.strip('\n'))
    print(new_mail_text)

# 4. Create new letter text files

# cwd is G:\Notes - 100 Days of Code\24 Day 24 - Intermediate - Files, Directories and Paths\Mail Merge Project Start

for i in names_list:
    with open(f"./Output/ReadyToSend/'Letter for {i}.txt", 'w') as output_file:
        output_file.write(new_mail_text)


# Now put it all together -

with open('./Input/Letters/starting_letter.txt') as file:
    mail_text = file.read()
    # print(mail_text)
    # no need to print now

with open('./Input/Names/invited_names.txt') as file:
    names_list = file.readlines()
    # first clue
    # print(names_list)
    # no need to print now

for i in names_list:
    name = i.strip('\n')
    # third clue
    # this is because later when we are creating new letters, the {i} in file path contains a new line char, i.e. \n
    # python interprets it as part of the file path
    new_mail_text = mail_text.replace('[name]', name)
    # second clue
    print(new_mail_text)
    with open(f"./Output/ReadyToSend/Letter for {name}.txt", 'w') as output_file:
        output_file.write(new_mail_text)


# 223 Solution & Walkthrough for the Mail Merge Project


# 224 What's the correct solution_ What's the best answer_ What's the right way_

