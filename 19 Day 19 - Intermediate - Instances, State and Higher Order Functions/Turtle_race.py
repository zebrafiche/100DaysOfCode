import turtle
import random

screen = turtle.Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput("Place your bet", "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

if user_bet in colors:
    game_on = True

    turtle_names = []
    for i in range(1, 7):
        turtle_names.append(f"turtle{i}")

    turtle_objects = []
    for t in turtle_names:
        t = turtle.Turtle(shape='turtle')
        turtle_objects.append(t)

    for i in range(6):
        turtle_objects[i].color(colors[i])

    y = -125
    for tims in turtle_objects:
        tims.penup()
        tims.goto(-230, y)
        y += 50

    while game_on:
        for tims in turtle_objects:
            tims.forward(random.randint(0, 10))
            if tims.xcor() > 230:
                # == will not work because
                # one moment a turtle's xcor() is 225, the next moment it is 231
                # in that case this block will not be triggered
                game_on = False
                if tims.color() == user_bet:
                    print('You win')
                else:
                    print(f"You Lose. {tims.pencolor()} won")
else:
    print(f"Sorry there is no {user_bet} colored turtle in the race")