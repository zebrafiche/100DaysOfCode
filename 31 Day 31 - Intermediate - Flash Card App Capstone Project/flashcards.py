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
