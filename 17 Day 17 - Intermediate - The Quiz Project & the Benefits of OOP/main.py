# 152 Day 17 Goals_ what we will make by the end of the day

# We will learn how to actually create the classes in the lesson
# We will be making a quiz game by the end of the day
# It will be a True/False quiz
# We will build it entirely by OOP, we'll build the classes ourselves and use it in the game


# 153 How to create your own Class in Python

# We have been using other people's classes so far
# Now it's time to make our own
# Last lesson had many classes, Menu(), Money_Machine(), Coffee_Machine() etc.
# From these classes we created objects, then called on the object's methods and attributes to get the desired results

# To build you own class, the syntax is -

class Rafi:
    # for now let's keep it empty, without any code in the indentation

# The class Rafi is currently empty
# But since it is a class afterall, we can create objects from it
# To create an object, we have to call on the class followed by a set of parenthesis
Rafi2 = Rafi()
# Now as you can see, in line 19, the indented comment after the class declaration, we have an error
# Because the class is empty
# How to bypass the error?

class Rafi:
    pass
Rafi2 = Rafi()

# No errors now

# Naming a class should have all the first letters of every word capitalized
# Like so - CarDashCam
# This style is known as PascalCase
# There is another style, camelCase, where the first letter is lowercase but every subsequent word has first letter capitalized
# Finally we have snake_case, where all the words are lowercase but they are separated by an underscore

# Usually, PascalCase is used to name classes, snake_case to name everything else


# 154 Working with Attributes, Class Constructors and the __init__() Function

class Rafi:
    pass
Rafi2 = Rafi()

# Now how do we create attributes?
# Just like we would create a variable, but separated with a dot notation from the object
Rafi2.name = 'abdullah_al_rafi'
Rafi2.wifename = 'mushsharat_rahman'

# But
# Doesn't this mean that everytime I create a new object
Rafi3 = Rafi()
# I will have to declare attributes again?
print(Rafi3.name)
# AttributeError: 'Rafi' object has no attribute 'name'

# We should, declare these inside the Class itself
# So that every object created from it behaves the same way with attributes and methods

# This is where constructor comes in, it is part of the blueprint that specifies what should happen when the object is constructed
# It is also called initialization, denoted by __init__

class Rafi:
    def __init__(self):
        # initialize attributes here
        print('rafi welcomes you...')
# So everytime you put anything under the initialization function, it will get triggered everytime an object is created

rafi2 = Rafi()
rafi3 = Rafi()
# rafi welcomes you...
# rafi welcomes you...

# Reminder - Attributes are things that the object will have. Basically variables associated with the final object
# For Rafi, they may be your height, represented by just a number
# So how do we set up these attributes in the constructor?

class Rafi:
    def __init__(self, height):
        self.height = height
        # so everytime a new object is created (rafi2) and the attribute is passed (rafi2.height), it will give the height
# height here is an additional parameter, that is still not set
# if we create an object passing something as the parameter, it will be used to create the attribute for that object

rafi2 = Rafi(178)
# the class now captures 178 and sets it as the height
print(rafi2.height)
# 178

# This is the same as -

class Rafi:
    def __init__(self):
        pass
rafi2 = Rafi()
rafi2.name = 'abdullah_al_rafi'
print(rafi2.name)
# abdullah_al_rafi

# We can also do this to change the attribute afterwards
class Rafi:
    def __init__(self, height):
        self.height = height
rafi2 = Rafi(5)
rafi2.height = 178
print(rafi2.height)
# 178

# Now imagine a scenario where we have to create multiple objects with different attributes, how can we do it?
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

# Note: When you create classes like this, where the attributes are defined
class Rafi:
    def __init__(self, height):
        self.height = height
# You must provide positional arguments when calling on the class while creating an object
rafi2 = Rafi()
rafi2.height = 179
print(rafi2.height)
# TypeError: Rafi.__init__() missing 1 required positional argument: 'height'

# We can also add attributes later

class Person:
    def __init__(self, name, wife):
        self.nametag = name
        self.spouse = wife
rafi = Person("Rafi", "Teetly")
rafi.color = 'Brown'
print(rafi.color)
# Brown
# What happens when you call on an attribute you don't have?
print(rafi.weight)
# AttributeError: 'Person' object has no attribute 'weight'

# We can declare some attributes during the initialization to a default value of 0
# That way they do not have to be passed as positional arguments when creating objects

class Person:
    def __init__(self, name, wife):
        self.nametag = name
        self.spouse = wife
        self.height = 0
        self.weight = 0

rafi = Person("Rafi", "Teetly")
print(rafi.nametag)
print(rafi.spouse)
print(rafi.height)
print(rafi.weight)

# Rafi
# Teetly
# 0
# 0


# 155 Adding Methods to a Class

# Attributes are the things that the object has
# Methods are the things that the object does

# Let's say that I now want to add a method that will allow me to follow another person

class Person:
    def __init__(self, name, wife):
        self.nametag = name
        self.spouse = wife
        self.height = 0
        self.weight = 0
        self.followers = 0
        self.followings = 0
    def follow(self,user):
        self.followings += 1
        user.followers += 1

# declare the obejcts first
rafi = Person("Rafi", "Teetly")
numayer = Person("Numayer", "Amy")

# call on the method on an object
rafi.follow(numayer)

# print results
print(rafi.followers)
print(rafi.followings)
print(numayer.followers)
print(numayer.followings)
# 0
# 1
# 1
# 0


# 156 Quiz Project Part 1_ Creating the Question Class

# A simple true/false game
# Download the zip file from the course resource in the project folder

# First task is to create a model for our question in the quiz

# We need to have a Question class, having attributes of text (the body of the ques) and the answer

class Question:
    def __init__(self, text, answer):
        self.body = text
        self.ans = answer


# 157 Quiz Project Part 2_ Creating the List of Question Objects from the Data

# Now we will be creating a question bank of question objects

# Creating a question object would look like this -
question = Question('q', 'a')

print(question.body)
print(question.ans)
# q
# a

# For a lot of questions, we need a list of question objects
# Sample -

# question_bank = [
#     Question(q1, a1),
#     Question(q2, a2),
#     Question(q3, a3)
# ]

# The zip folder contains a file called data, download that in the project folder
# It is nothing but a list of questions

# Now the data is inside distionaries inside a list
# And they are not indented
# Quick Tip - Select the code goto code > auto indent lines
# Some errors are still showing because the lines are too long, just press Enter on a good spot and PyCharm will take care

# Now we need to convert the question_data list from the data file into this format -
# question_bank = [
#     Question(q1, a1),
#     Question(q2, a2),
#     Question(q3, a3)
# ]

class Question:
    def __init__(self, text, answer):
        self.body = text
        self.ans = answer

import data
question_bank = []
for i in data.question_data:
    question_bank.append(Question(i['text'], i['answer']))
print(question_bank)

# [<__main__.Question object at 0x00000227335CF2E0>, <__main__.Question object at 0x00000227335CDB10>,
# <__main__.Question object at 0x00000227335CE650>, <__main__.Question object at 0x00000227335CD870>,
# <__main__.Question object at 0x00000227335CD960>, <__main__.Question object at 0x00000227335CDD20>,
# <__main__.Question object at 0x00000227335CDD80>, <__main__.Question object at 0x00000227335CEC20>,
# <__main__.Question object at 0x00000227335CEBC0>, <__main__.Question object at 0x00000227335CEB60>,
# <__main__.Question object at 0x00000227335CEB00>, <__main__.Question object at 0x00000227335CEAA0>]

print(question_bank[0].body)
print(question_bank[0].ans)
# A slug's blood is green.
# True

# Perfect so far


# 158 Quiz Project Part 3_ The QuizBrain and the next_question() Method

# Now create a QuizBrain class
# Will have attributes - question_number and question_list
# Will have method, next_question, which will pull up the next question in the list

# In the lesson, the Question class and the Quizbrain class were created in separate files
# And then those modules were imported
# I guess to compartmentalize the problem
# But I need everything on one sheet for note-taking purpose, so doing here

class Question:
    def __init__(self, text, answer):
        self.body = text
        self.ans = answer

import data
question_bank = []
for i in data.question_data:
    question_bank.append(Question(i['text'], i['answer']))

# Now

class QuizBrain:
    def __init__(self, q_bank):
        # self.question_number is going to have a default value so no need to put it as an input while creating object
        self.question_number = 0
        self.question_list = q_bank

# We will pass over the question bank as an input while creating the object, and the object will have a question_bank attribute

# Now we have to create a method that gets the question from the list and asks an input (T/F) from the user
# Also increment the question number by one
    def next_question(self):
        question_text = self.question_list[self.question_number].body
        self.question_number += 1
        input(f"Q.{self.question_number}: {question_text} (True/False): ")

# Now the QuizBrain class is done

# Let's create a quiz object
quiz = QuizBrain(question_bank)
quiz.next_question()

# Execute -
# Q.0: A slug's blood is green. (True/False):
# Q.0?? - Change the input so that it shows the question number, not the index number
# Q.1: A slug's blood is green. (True/False):

# But it only asks once, how do we make it keep going? Also there needs to be a score counter


# 159 Quiz Project Part 4_ How to continue showing new Questions

# While loop required
# Also we need another method in the QuizBrain class that checks if there are questions left in the question bank

class Question:
    def __init__(self, text, answer):
        self.body = text
        self.ans = answer

import data
question_bank = []
for i in data.question_data:
    question_bank.append(Question(i['text'], i['answer']))

class QuizBrain:
    def __init__(self, q_bank):
        # self.question_number is going to have a default value so no need to put it as an input while creating object
        self.question_number = 0
        self.question_list = q_bank

    def next_question(self):
        question_text = self.question_list[self.question_number].body
        self.question_number += 1
        input(f"Q.{self.question_number}: {question_text} (True/False): ")

# Add the method:

    def still_has_questions(self):
        if 0 <= self.question_number < len(self.question_list):
            return True
        else:
            return False
        # QuickTip - We could get the same effect by writing this - return 0 <= self.question_number <= len(self.question_list)

# Now create the object, the while loop with the method and the method inside
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# It goes on until the questions run out
# We still need to check the answers and have a score counter


# 160 Quiz Project Part 5_ Checking Answers and Keeping Score

# We will need to add another method to QuizBrain, that checks answer, and another attribute that keeps score

class Question:
    def __init__(self, text, answer):
        self.body = text
        self.ans = answer

import data
question_bank = []
for i in data.question_data:
    question_bank.append(Question(i['text'], i['answer']))

class QuizBrain:
    def __init__(self, q_bank):
        # self.question_number is going to have a default value so no need to put it as an input while creating object
        self.question_number = 0
        # add a score attribute
        self.score = 0
        self.question_list = q_bank

    def next_question(self):
        question_text = self.question_list[self.question_number].body
        # add a variable called current_answer
        current_answer = self.question_list[self.question_number].ans
        self.question_number += 1
        # rename the input below into user_answer
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # call on the check answer method, so that the answers will be checked until the while loop is in effect
        self.check_answer(user_answer, current_answer)

    def still_has_questions(self):
        if 0 <= self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Good')
            self.score += 1
        else:
            print('Bad')
        print(f"Your current score is {self.score}/{self.question_number}")
        print('\n')


# Now create the object, the while loop with the method and the method inside
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz. Your final score is {quiz.score}/{len(quiz.question_list)}")


# 161 The Benefits of OOP_ Use Open Trivia DB to Get New Questions

# Boring if it is the same questions right?
# Open Trivia Database - Link in course resources
# Go there, click API, select preferences, generate API url
# You will get the JSON (Javascript Object Notation) text
# Copy and paste it in data
# Select all, click code, reformat code
# You will get a list with dictionaries, just like the old data, with two keys named "question" and "correct_answer"
# How to modify the code so that it works with the changed keynames?

class Question:
    def __init__(self, text, answer):
        self.body = text
        self.ans = answer

import data
question_bank = []
for i in data.question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))

class QuizBrain:
    def __init__(self, q_bank):
        # self.question_number is going to have a default value so no need to put it as an input while creating object
        self.question_number = 0
        # add a score attribute
        self.score = 0
        self.question_list = q_bank

    def next_question(self):
        question_text = self.question_list[self.question_number].body
        # add a variable called current_answer
        current_answer = self.question_list[self.question_number].ans
        self.question_number += 1
        # rename the input below into user_answer
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # call on the check answer method, so that the answers will be checked until the while loop is in effect
        self.check_answer(user_answer, current_answer)

    def still_has_questions(self):
        if 0 <= self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Good')
            self.score += 1
        else:
            print('Bad')
        print(f"Your current score is {self.score}/{self.question_number}")
        print('\n')


# Now create the object, the while loop with the method and the method inside
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


# IT WORKS!!!
# That is the beauty of OOP, we did not need to touch other modules, just a simple tweak in the keynames did the job
# This is modularity at its best


# 162 Run for that Bus!

