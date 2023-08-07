import turtle

sketcher = turtle.Turtle()
screen = turtle.Screen()


def move_forwards():
    sketcher.forward(10)


def move_backwards():
    sketcher.back(10)


def move_left():
    sketcher.left(10)


def move_right():
    sketcher.right(10)


def clear():
    sketcher.clear()
    sketcher.penup()
    sketcher.home()
    sketcher.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()