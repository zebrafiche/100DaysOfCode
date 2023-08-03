# 301 Day 34 Goals_ what you will make by the end of the day

# Today we will be working with a little bit of review
# We will use the open trivia database API for this
# And we will use the tkinter app for the GUI


# 302 Trivia Question API Challenge

# Modify the quiz game using the API from the opentriviadatabase.com
# The API endpoint is everything before the question mark
# After the question mark we have the parameters

# Now you have unpacked the starting files for the quiz game
# In that quiz game, we had a separate data file containing all the question data
# IT basically contained a list of the possible questions
# We want to instead have the questions through an API

# Todo 1 - get the API
import requests
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

# Todo 2 - decode the API
# convert the response object into json()
data = response.json()
print(data)
# {'response_code': 0, 'results': [{'category': 'Entertainment: Television', .....
# Todo 3 - plug the API in the question bank
print(data['results'])
# to pretty print, we can use the json module
# json.dumps() to pretty print
# the dumps() method returns a json formatted string from the json object
# the indent parameter is used to define the indent level
import json
question_data = json.dumps(data['results'], indent=1)
print(question_data)

# [
# {
#  "category": "Entertainment: Television",
#  "type": "boolean",
#  "difficulty": "medium",
#  "question": "AMC&#039;s &quot;The Walking Dead&quot;, Rick, Carl, Daryl, Morgan, Carol ...",
#  "correct_answer": "False",
#  "incorrect_answers": [
#   "True"
#  ]
# },
# {
#  "category": "General Knowledge",
#  "type": "boolean",
#  "difficulty": "medium",
#  "question": "&quot;Typewriter&quot; is the longest word that can be typed using only the first row ...",
#  "correct_answer": "True",
#  "incorrect_answers": [
#   "False"
#  ]
# },


# 303 Solution & Walkthrough for getting Trivia Questions

import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']
# it may be that doing the json dumps thing messes up the formatting, which is why it does not work
# just storing data['results'] in the variable question_data works fine


# 304 Unescaping HTML Entities

# these strange formatting where single and doubel quotes are shown as &#039; and &quot;
# you can see what these texts actually mean by suing freeformatter

# a google search takes us to stack overflow
# where we see how to unescape these formatted texts in the code
import html
q_text = html.unescape("&quot;Typewriter&quot; is the longest word that can be typed using only the first row ...")
print(q_text)
# "Typewriter" is the longest word that can be typed using only the first row ...

# the required changes will need to be done in quiz_brain

import html

formatted_q_text = html.unescape(self.current_question.text)
user_answer = input(f"Q.{self.question_number}: {formatted_q_text} (True/False): ")


# 305 Class based Tkinter UI

# Timestamp - 05:30


# 306 Python Typing & Showing the Next Question in the GUI
# in the ui.py file -
from quiz_brain import QuizBrain
class QuizInterface:
    # How do we get the same Quizbrain instance that we created in our main.py?
    # Otherwise if we create another instance of Quizbrain here the questions might be different
    # You do it like this, in main.py -
    # quiz = QuizBrain(question_bank)
    # quiz_ui = QuizInterface(quiz)
    # So now the quiz_ui object has the same QuizBrain instance created in main.py
    # So this now means that the QuizInterface now takes a QuizBrain object as an argument

    # though we have passed in quiz_brain as an argument, QuizInterface still doesn't know what quiz_brain is
    # so to let it know we have to import QuizBrain
    # and then when we declare that quiz_brain is a QuizBrain object
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # to let the entire question fit into the canvas, set the width of the text a bit lower than the canvas width
        self.question_text = self.canvas.create_text(200, 200, text="Hello", width=200, font=('Courier', 15, 'bold'))

        self.get_next_question()

    # How do we get the same Quizbrain instance that we created in our main.py?
    # Otherwise if we create another instance of Quizbrain here the questions might be different
    # You do it like this, in main.py -
    # quiz = QuizBrain(question_bank)
    # quiz_ui = QuizInterface(quiz)
    # So now the quiz_ui object has the same QuizBrain instance created in main.py
    # So this now means that the QuizInterface now takes a QuizBrain object as an argument

    def get_next_question(self):
        new_question_text = self.quiz.next_question()
        # as you type this line above, nothing shows up
        # bcz though we have passed in quiz_brain as an argument, QuizInterface still doesn't know what quiz_brain is
        # so to let it know we have to import QuizBrain
        # and then when we declare that quiz_brain is a QuizBrain object
        self.canvas.itemconfig(self.question_text, text=new_question_text)


# in the main.py file -
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


# 307 Python Typing_ Type Hints and Arrows -_
# let's say you are doing a survey where you are finding ages of a certain sample
# you can declare the type of the variable age before hand
age: int

# afterwards if you try to assign a string to the variable age -
# age= 'yes'
# does not work, py charm tells you that it should be an int

# also works in functions
def police_check(driver_age: int):
    if driver_age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

# this way if you type anything wrong during calling the function, it will tell you
# police_check("twelve")
# pycharm tells us that it expected type int and got str

# Similarly we can also specify the type of the output of a function, just like the input
def police_check(driver_age: int) -> bool:
    if driver_age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

# This particular feature is called "type hint" in python


# 308 Check the Answer
# In the quiz_brain.py file -
# The check_answer method takes an input
def check_answer(self, user_answer):
    correct_answer = self.current_question.answer
    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        print("You got it right!")
    else:
        print("That's wrong.")

# so in the ui.py file -

def input_true(self):
    self.user_answer = 'True'
    self.quiz.check_answer(self.user_answer)
    # when the user presses a button the next question should generate


def input_false(self):
    self.user_answer = 'False'
    self.quiz.check_answer(self.user_answer)
    # when the user presses a button the next question should generate

self.true_button.config(command=self.input_true)
self.false_button.config(command=self.input_false)


# 309 Give Feedback to the Player, Keep Score and Fix the Bugs =)
