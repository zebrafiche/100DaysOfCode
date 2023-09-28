from turtle import Screen
import time
import snake
import food
import scoreboard
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title("Rafi's snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
food.refresh()
points = scoreboard.scoreboard()
screen.update()


# def move_right():
#     turtle1.setheading(0)
#
#
# def move_left():
#     turtle1.setheading(180)
#
#
# def move_up():
#     turtle1.setheading(90)
#
#
# def move_down():
#     turtle1.setheading(270)


screen.listen()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
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


screen.exitonclick()
