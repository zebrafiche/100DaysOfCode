import pandas
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
        undiscovered_states = [i for i in states_list if i not in correct_answers_list]
        # undiscovered_states = []
        # for i in states_list:
        #     if i not in correct_answers_list:
        #         undiscovered_states.append(i)
        # undiscovered_states = {
        #     'states_not_guessed': undiscovered_states
        # }
        # no need to create the dict, just feed the list to pandas, that will also do
        us_df = pandas.DataFrame(undiscovered_states)
        us_df.to_csv('undiscovered_states.csv')
        break
screen.exitonclick()
