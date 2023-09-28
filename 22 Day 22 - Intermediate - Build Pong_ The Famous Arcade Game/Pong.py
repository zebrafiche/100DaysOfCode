
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()


screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
# Turn turtle animation on/off and set delay for update drawings.
# If n is given, only each n-th regular screen update is really performed.

block1 = Paddle((350, 0))
block2 = Paddle((-350, 0))
pong = Ball()
score1 = Scoreboard()
score1.goto(0, 280)
score1.write(f'Player 1 score - {score1.score}', move=False, align='center', font=('Courier', 10, 'bold'))
score2 = Scoreboard()
score2.goto(0, -280)
score2.write(f'Player 2 score - {score1.score}', move=False, align='center', font=('Courier', 10, 'bold'))

# block1 = Turtle()
# block1.penup()
# block1.shape('square')
# block1.color('white')
#
# block1.resizemode('user')
# block1.shapesize(stretch_wid=5, stretch_len=1)
# block1.goto(x=380, y=0)

# screen.update()
# setting screen update here will only manually update when block1 is here,
# and no more animation after that, so you will not see yourself controlling the paddle

screen.listen()
screen.onkey(block1.up, key="Up")
screen.onkey(block1.down, key="Down")
screen.onkey(block2.up, key="w")
screen.onkey(block2.down, key="s")

# instead
game_on = True
while game_on:
    time.sleep(pong.move_speed)
    pong.move()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()

    if pong.xcor() > 320 and pong.distance(block1) < 50 or pong.xcor() < -320 and pong.distance(block2) < 50:
        # pong.increase_speed()
        pong.ricochet()

    if pong.xcor() > 380:
        pong.home()
        pong.bounce()
        pong.ricochet()
        pong.move_speed = 0.1
        score2.score += 1
        score2.clear()
        score2.write(f'Player 2 score - {score2.score}', move=False, align='center', font=('Courier', 10, 'bold'))

    if pong.xcor() < -380:
        pong.home()
        pong.bounce()
        pong.ricochet()
        pong.move_speed = 0.1
        score1.score += 1
        score1.clear()
        score1.write(f'Player 1 score - {score1.score}', move=False, align='center', font=('Courier', 10, 'bold'))

    screen.update()


screen.exitonclick()
