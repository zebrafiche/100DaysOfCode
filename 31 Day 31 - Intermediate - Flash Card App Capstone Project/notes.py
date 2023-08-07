# 277 Day 31 Goals_ what you will make by the end of the day

# By the end of the day, you will have built a flashcard program

# 1. A card appears
# 2. 3 seconds later, the card disappears and another card appears with the meaning of the word
# 3. There are two buttons a right and a wrong button
# 4. If you have gotten the answer, you press right, otherwise, press wrong
# 5. The button clicks keeps tally
# 6. Once you click the check mark, that word gets removed from the list of words to be shown


# 278 Step 1 - Create the User Interface (UI) with Tkinter
# 279 Solution & Walkthrough for Creating the UI

# 1. import modules
from tkinter import *
import pandas
import random

# a.     create variables
sec = 3
BG = "#b1ddc6"

# 2. create canvas
screen = Tk()
screen.title('Flashcards')
screen.config(bg=BG, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BG, highlightthickness=0)

# 3. add photo to canvas
#     a. front side
front_side = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=front_side)

#     b. back side
back_side = PhotoImage(file="card_back.png")
canvas.create_image(400, 263, image=back_side)

canvas.grid(column=0, row=0, columnspan=2)

# 5. add text to canvas, from the dataframe
word_list = french_df["French"]
random_word = random.choice(word_list)
answer_row = french_df[french_df["French"] == random_word]
the_answer = answer_row.English.item()
# French
canvas.create_text(400, 150, text="French", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text=random_word, font=('Ariel', 60, 'bold'))
# English
canvas.create_text(400, 150, text="English", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text=the_answer, font=('Ariel', 60, 'bold'))

# 6. add buttons
#     a. right button
check_mark = PhotoImage(file="right.png")
check_button = Button(image=check_mark, highlightthickness=0, borderwidth=0)
check_button.grid(column=0, row=1)

#     b. wrong button
cross_mark = PhotoImage(file="wrong.png")
cross_button = Button(image=cross_mark, highlightthickness=0, borderwidth=0)
cross_button.grid(column=1, row=1)

# highlightthickness and borderwidth to remove the borders around the button

screen.mainloop()


# 280 Step 2 - Create New Flash Cards
# 281 Solution & Walkthrough for Creating New Flash Cards

# changes -

# 4. import csv and create dataframe
french_df = pandas.read_csv("french_words.csv")
words_dict = french_df.to_dict(orient='records')

# there are different ways to orient the dictionary, I am using records
# print(words_dict)
# [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}...

# 5. add text to canvas, from the dataframe

# French
random_item = random.choice(words_dict)
canvas.create_text(400, 150, text="French", font=('Ariel', 40, 'italic'))
french_text = canvas.create_text(400, 263, text=random_item['French'], font=('Ariel', 60, 'bold'))

# English
canvas.create_text(400, 150, text="English", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text=random_item["English"], font=('Ariel', 60, 'bold'))

# 8. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.

def new_word():
    global random_item
    random_item = random.choice(words_dict)
    canvas.itemconfig(french_text, text=random_item['French'])

# 7. create function so that when right button is clicked, the word is erased
mastered_list = []

def mastered():
    global random_item
    mastered_list.append(random_item)
    words_dict.remove(random_item)
    new_word()


# 282 Step 3 - Flip the Cards!
# 283 Solution & Walkthrough for Flipping Cards

# changes -

back_side = PhotoImage(file="card_back.png")
canvas.create_image(400, 263, image=back_side)

front_side = PhotoImage(file="card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_side)

def flip_back():
    canvas.itemconfig(canvas_image, image=back_side)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(current_word, text=random_item["English"], fill='white')
def flip_front():
    canvas.itemconfig(canvas_image, image=front_side)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(current_word, text=random_item["French"], fill='black')

def new_word():
    global random_item
    random_item = random.choice(words_dict)
    screen.after_cancel(timer)  # this cancels the timer
    flip_front()  # this flips the card
    screen.after(3000, flip_back)  # this restarts the timer

timer = screen.after(3000, flip_back)  # this flips the first card

screen.mainloop()


# 284 Step 4 - Save Your Progress
# 285 Solution & Walkthrough for Saving Progress

# Add to csv the words_mastered when check button is clicked
updated_df = pandas.DataFrame(words_mastered)
updated_df.to_csv('./mastered.csv', index=False)
# index=False so that the output contains only two columns, French and English

# this words mastered will be reset everytime we run, since
# words_mastered = [] at the beginning
mastered_df = pandas.read_csv('mastered.csv')
words_mastered = mastered_df.to_dict(orient='records')
# what if there is no mastered.csv?
try:
    mastered_df = pandas.read_csv('mastered.csv')
    words_mastered = mastered_df.to_dict(orient='records')
except FileNotFoundError:
    words_mastered = []

# In addition we need to do the same for the words to learn
updated_df2 = pandas.DataFrame(words_to_learn)
updated_df2.to_csv('to_learn.csv', index=False)
# and
try:
    to_learn_df = pandas.read_csv('to_learn.csv')
except FileNotFoundError:
    french_df = pandas.read_csv("french_words.csv")
    words_to_learn = french_df.to_dict(orient='records')
else:
    words_to_learn = to_learn_df.to_dict(orient='records')


# That, is it
# Putting everything together

# TODO 1. import modules
from tkinter import *
import pandas
import random

# a.     create variables
BG = "#b1ddc6"

# TODO 2. create canvas
screen = Tk()
screen.title('Flashcards')
screen.config(bg=BG, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BG, highlightthickness=0)

# TODO 3. add photo to canvas

#     b. back side
back_side = PhotoImage(file="card_back.png")
canvas.create_image(400, 263, image=back_side)

#     a. front side
front_side = PhotoImage(file="card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_side)

# Rearranging so the canvas starts off with the front side

canvas.grid(column=0, row=0, columnspan=2)

#     c. make it so that the back side gets displayed after 3 seconds, flipping


def flip_back():
    canvas.itemconfig(canvas_image, image=back_side)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(current_word, text=random_item["English"], fill='white')


def flip_front():
    canvas.itemconfig(canvas_image, image=front_side)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(current_word, text=random_item["French"], fill='black')


# TODO 4. import csv and create dataframe

try:
    mastered_df = pandas.read_csv('mastered.csv')
    words_mastered = mastered_df.to_dict(orient='records')
except FileNotFoundError:
    words_mastered = []

try:
    to_learn_df = pandas.read_csv('to_learn.csv')
except FileNotFoundError:
    french_df = pandas.read_csv("french_words.csv")
    words_to_learn = french_df.to_dict(orient='records')
else:
    words_to_learn = to_learn_df.to_dict(orient='records')

# there are different ways to orient the dictionary, I am using records
# print(words_dict)
# [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}...

# TODO 5. add text to canvas, from the dataframe

# French (to start with)
random_item = random.choice(words_to_learn)
card_title = canvas.create_text(400, 150, text="French", font=('Ariel', 40, 'italic'))
current_word = canvas.create_text(400, 263, text=random_item['French'], font=('Ariel', 60, 'bold'))

# English
# canvas.create_text(400, 150, text="English", font=('Ariel', 40, 'italic'))
# canvas.create_text(400, 263, text=random_item["English"], font=('Ariel', 60, 'bold'))

# TODO 8. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.


def new_word():
    global random_item
    random_item = random.choice(words_to_learn)
    screen.after_cancel(timer)
    flip_front()
    screen.after(3000, flip_back)

# TODO 7. create function so that when right button is clicked, the word is erased


def mastered():
    global random_item
    words_mastered.append(random_item)
    updated_df = pandas.DataFrame(words_mastered)
    updated_df.to_csv('mastered.csv', index=False)
    words_to_learn.remove(random_item)
    updated_df2 = pandas.DataFrame(words_to_learn)
    updated_df2.to_csv('to_learn.csv', index=False)
    new_word()
    print(len(words_mastered))
    print(len(words_to_learn))


# TODO 6. add buttons

#     a. right button
check_mark = PhotoImage(file="right.png")
check_button = Button(image=check_mark, highlightthickness=0, borderwidth=0, command=mastered)
check_button.grid(column=0, row=1)

#     b. wrong button
cross_mark = PhotoImage(file="wrong.png")
cross_button = Button(image=cross_mark, highlightthickness=0, borderwidth=0, command=new_word)
cross_button.grid(column=1, row=1)

# highlightthickness and borderwidth to remove the borders around the button

timer = screen.after(3000, flip_back)

screen.mainloop()
