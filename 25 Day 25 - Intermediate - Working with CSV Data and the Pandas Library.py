# 225 Day 25 Goals_ what we will make by the end of the day

# today we will learn about how to work with csv files
# and analyzing the data with a library called Pandas

# by the end of the day we will have built an educational quiz game about the states of the US


# 226 Reading CSV Data in Python

# we will be working with a csv files named weather data.csv
# open it in pycharm
# once you do pycharm recognizes it as a csv file and asks you to install plugins
# click cancel because we want to view the files as raw data

# csv stands for comma separated values

# when opened in pycharm, the raw data looks like this -
# day,temp,condition
# Monday,12,Sunny
# Tuesday,14,Rain
# Wednesday,15,Rain
# Thursday,14,Cloudy
# Friday,21,Sunny
# Saturday,22,Sunny
# Sunday,24,Sunny

# challenge - create a list called data containing each line in the waether-data.csv as a list item

# 1. find the method from the last day's lesson
# got it, readlines()

# 2. apply here
with open('./weather-data.csv') as file:
    data = file.readlines()
    print(data)

# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n',
#  'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

# to get rid of the newline characters -
data = []
with open('./weather-data.csv') as file:
    for i in file.readlines():
        data.append(i.strip('\n'))
print(data)

# ['day,temp,condition', 'Monday,12,Sunny', 'Tuesday,14,Rain', 'Wednesday,15,Rain', 'Thursday,14,Cloudy',
#  'Friday,21,Sunny', 'Saturday,22,Sunny', 'Sunday,24,Sunny']

# but the data in this list, every item is still separated by commas, will be hard to work with this file

# alternative -
# there is a library to work with csv files, import it

import csv
with open('./weather-data.csv') as file:
    data = csv.reader(file)
    print(data)
    # <_csv.reader object at 0x0000021226F9B280>
    for row in data:
        print(row)
# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny']
# ['Tuesday', '14', 'Rain']
# ['Wednesday', '15', 'Rain']
# ['Thursday', '14', 'Cloudy']
# ['Friday', '21', 'Sunny']

# challenge - now, get all the temperature data in integer format in a separate list called temperatures

import csv
with open('./weather-data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
print(temperatures)

# [12, 14, 15, 14, 21, 22, 24]

# the csv library is good, but
# imagine a data set with lots of columns, lots of complex data
# imagine you want to get hold of the data in column AAB in each row
# how would you find the index number then?
#
# this is where Pandas comes in

# Pandas is a super powerful python data analysis library

# shortcut - just type import pandas, and hover over the red line to get the prompt to install the package
import pandas
# the method you can read csv files with is read.csv
data = pandas.read_csv('./weather-data.csv')
print(data)

#         day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

print(data['temp'])

# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24


# 227 DataFrames & Series_ Working with Rows & Columns
# to check what type of file data is -
print(type(data))
# <class 'pandas.core.frame.DataFrame'>

# it is a dataframe object

# in the documentation they talk about two primary data structure of pandas, series and dataframe
# every sheet is considered a dataframe in pandas

# what is a series object then?

print(type(data['temp']))
# <class 'pandas.core.series.Series'>

# so the whole table is dataframe and the column is series

# let's explore the documentation
# documentation > API reference > DataFrame > serialization/IO conversion > DataFrame.to_dict

data_dict = data.to_dict()
print(data_dict)

# {
#     'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#     'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#     'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
# }


# documentation > API reference > Series > Conversion > Series.to_list

temp_list = data['temp'].to_list()
print(temp_list)

# [12, 14, 15, 14, 21, 22, 24]

# challenge - calculate the average temperature in your series of temperatures

# using google - Series.mean()
# documentation > API reference > Series > Computations/descriptive stats > Series.mean()
print(data['temp'].mean())

# 17.428571428571427

# challenge - get the maximum value in your series of temperatures
# documentation > API reference > Series > Computations/descriptive stats > Series.max()
print(data['temp'].max())

# 24

print(data['condition'])
# here it is as if you are using it as a dictionary and calling the items by the key 'condition'

# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny

# instead of using square brackets (data['condition']) we can also use data.condition
# so data is our object, right?
# the fact that we can call data.function means that when we created the object data, panda took all columns
# and turned them into separate attributes
# pretty powerful

print(data.condition)
# here it is as if you are treating it as an object, calling on the attribute 'condition'

# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny

# how to get data in the rows?

print(data[data.day == 'Monday'])

#       day  temp condition
# 0  Monday    12     Sunny

print(data.loc[data.day == 'Monday'])

#       day  temp condition
# 0  Monday    12     Sunny

print(data[data.temp >= 20])

#         day  temp condition
# 4    Friday    21     Sunny
# 5  Saturday    22     Sunny
# 6    Sunday    24     Sunny

print(data.loc[data.temp >= 20])

#         day  temp condition
# 4    Friday    21     Sunny
# 5  Saturday    22     Sunny
# 6    Sunday    24     Sunny

# challenge - which row had the max temperature?

print(data[data.temp == data.temp.max()])

#       day  temp condition
# 6  Sunday    24     Sunny

print(data[data.temp == data.temp.max()])

#       day  temp condition
# 6  Sunday    24     Sunny

# if we only put the name of the column we get the entire column (data.condition)
# but if we put specify a criteria in that column then we get the entire row

# what if we have a row but want to get a particular criteria for that day, i.e. temp?

monday = data[data.day == 'Monday']
print(monday.temp)

# 0    12

# challenge - get monday's temperature but in Fahrenheit

monday_temp_F = int(monday.temp) * 9/5 + 32
print(monday_temp_F)

# 53.6

# Create a dataframe from scratch

# imagine you have a dictionary -

student_dict = {
    "students" : ['Amy', 'James', 'Angela'],
    "scores" : [76, 36, 65]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

#   students  scores
# 0      Amy      76
# 1    James      36
# 2   Angela      65

student_df.to_csv('./student_df.csv')

# you can see that the project folder now has a new file called student_df.csv


# 228 The Great Squirrel Census Data Analysis (with Pandas!)

# 1. import the csv to pandas
import pandas
data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
# print(data['Primary Fur Color'])

# 2. filter fur color
types_of_fur = data['Primary Fur Color'].unique()
print(types_of_fur)
# [nan 'Gray' 'Cinnamon' 'Black']
print(types_of_fur[1:])

occurrences = []
for color in types_of_fur[1:]:
    occurrences.append(data['Primary Fur Color'].value_counts()[f"{color}"])
print(occurrences)

# 3. export to another dataframe
fur_colors = {
    'colors': types_of_fur[1:],
    'occurrences': occurrences
}
# 4. export the dataframe to csv
fur_colors_df = pandas.DataFrame(fur_colors)
print(fur_colors_df)

#      colors  occurrences
# 0      Gray         2473
# 1  Cinnamon          392
# 2     Black          103


# Instructor's method -

import pandas
data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
print(df)

#   Fur Color  Count
# 0      Gray   2473
# 1  Cinnamon    392
# 2     Black    103


# 229 U.S. States Game Part 1_ Setup

import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')

# for convenience, get the image file in a variable
image_path = 'blank_states_img.gif'

# from the turtle docs -
# turtle.register_shape(name, shape=None)
# turtle.addshape(name, shape=None)¶
#
# name is the name of a gif-file and shape is None:
# Installs the corresponding image shape.

screen.addshape(image_path)
turtle.shape(image_path)

# now when you run it you can see that the turtle has assumed the shape of the image

# # now we want to get the x, y coordinates of every state
# # we can do that by clicking on the state and getting its coordinates
#
# # turtle.onscreenclick(fun, btn=1, add=None)
# # fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
# # meaning the method takes a function with two arguments, what arguments? the x, y of the click location
# # meaning the method feeds the x, y coordinates of the click into the function with two arguments
#
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# # instead of screen.exitonclick() use turtle.mainloop() so that it will stay on the screen even after clicking
# turtle.mainloop()


# x, y coordinates have been provided in the csv file, pull the data from there instead

# ask the user for input
answer_state = screen.textinput(title='Guess the State', prompt="What's another state name?")

screen.exitonclick()


# 230 U.S. States Game Part 2_ Challenge with .csv

# 1. check the user's answer against the input
import pandas
states_data = pandas.read_csv('50_states.csv')
states_list = states_data['state'].to_list()
print(states_list)

formatted_answer = answer_state.title()
correct_answers_list = []
if formatted_answer in states_list:
    # code

# 2. state name should be generated in its corresponding x, y coordinate, if wrong, nth happens
if formatted_answer in states_list:
    correct_answers_list.append(formatted_answer)
    answer_row = states_data[states_data['state'] =='Ohio']
    print(answer_row)
    x = int(answer_row['x'])
    y = int(answer_row['y'])
    answer_turtle = turtle.Turtle()
    answer_turtle.hideturtle()
    answer_turtle.penup()
    answer_turtle.goto(x, y)
    answer_turtle.write(f"{formatted_answer}", False, 'center')

# 3. in the input box title, keep score of the correct guesses
answer_state = screen.textinput(title=f"Guess the State ({len(correct_answers_list)/len(states_list)})", prompt="What's another state name?")


# Keep Looping until he gets a wrong guess
game_on = True
while game_on:
    if formatted_answer in states_list:
        # code
    else:
        game_on = False

# Now put it all together

import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')

image_path = 'blank_states_img.gif'

screen.addshape(image_path)
turtle.shape(image_path)

states_data = pandas.read_csv('50_states.csv')
states_list = states_data['state'].to_list()
correct_answers_list = []

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"Guess the State ({len(correct_answers_list)}/{len(states_list)})",
                                    prompt="What's another state name?")
    formatted_answer = answer_state.title()

    if formatted_answer in states_list:
        correct_answers_list.append(formatted_answer)
        answer_row = states_data[states_data['state'] == formatted_answer]
        print(answer_row)
        x = int(answer_row['x'])
        y = int(answer_row['y'])
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_turtle.goto(x, y)
        # Series.item()[source]
        # Return the first element of the underlying data
        # answer_turtle.write(f"{answer_row.state.item()}", False, 'center')
        answer_turtle.write(f"{formatted_answer}", False, 'center')
    else:
        game_on = False

screen.exitonclick()


# 231 U.S. States Game Part 3_ Saving Data to .csv

# 1. do not end the game when the user guesses wrong, rather when he types Exit
if formatted_answer == 'Exit':
    break
# 2. generate a csv in the project folder containing all the states that he could not guess
undiscovered_states = []
for i in states_list:
    if i not in correct_answers_list:
        undiscovered_states.append(i)
undiscovered_states = {
    'states_not_guessed': undiscovered_states
}

us_df = pandas.DataFrame(undiscovered_states)
us_df.to_csv('undiscovered_states.csv')

# Now put it all together

import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')

image_path = 'blank_states_img.gif'

screen.addshape(image_path)
turtle.shape(image_path)

states_data = pandas.read_csv('50_states.csv')
states_list = states_data['state'].to_list()
correct_answers_list = []

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"Guess the State ({len(correct_answers_list)}/{len(states_list)})",
                                    prompt="What's another state name?")
    formatted_answer = answer_state.title()

    if formatted_answer in states_list:
        correct_answers_list.append(formatted_answer)
        answer_row = states_data[states_data['state'] == formatted_answer]
        print(answer_row)
        x = int(answer_row['x'])
        y = int(answer_row['y'])
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_turtle.goto(x, y)
        # Series.item()[source]
        # Return the first element of the underlying data
        # answer_turtle.write(f"{answer_row.state.item()}", False, 'center')
        answer_turtle.write(f"{formatted_answer}", False, 'center')
    # else:
    #     game_on = False

    if formatted_answer == 'Exit':
        undiscovered_states = []
        for i in states_list:
            if i not in correct_answers_list:
                undiscovered_states.append(i)
        # undiscovered_states = {
        #     'states_not_guessed': undiscovered_states
        # }
        # no need to create the dict, just feed the list to pandas, that will also do
        us_df = pandas.DataFrame(undiscovered_states)
        us_df.to_csv('undiscovered_states.csv')
        break
screen.exitonclick()


# fin, no motivational video today