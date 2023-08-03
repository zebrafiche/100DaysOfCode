# 196 Day 22 Goals_ what you will make by the end of the day

# Pong game, you know it by the name dx-ball
# Tasks -
# 1. Make the screen
# 2. Make the paddles for the two players
# 3. Use onkey so the paddles can be moved with up and down
# 4. Place the paddles on the right and left edge of the screen
# 5. Create a moving ball that bounces off of surfaces
#     a. detect collision with screen edges
#     b. detect collision with paddles
#     c. create angular deflection
# 6. Detect when paddle misses
# 7. Create scoreboard that keeps scores with every bounce (class)
# 8. Create a line through the middle of the screen

# Instructor suggested tasks
# 1. Make the screen
# 2. Create a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses


# 197 Set up the Main Screen

from turtle import Screen
screen = Screen()
# screen.screensize(canvwidth=1200, canvheight=600)
# cannot use screensize here
# The screensize() method sets the amount of area the turtle can roam,
# but doesn't change the screen size (despite the name), just the scrollable area
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.exitonclick()


# 198 Create a Paddle that responds to Key Presses

# create a separate file paddle, in it create a class Paddle
from turtle import Turtle
# a. create a block
block1 = Turtle()
block1.penup()
block1.shape('square')
block1.color('white')

# in the paddle file do this same thing but like this
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')

# b. make three other blocks
# instead of making three other separate turtles, we could just stretch this one
# turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
block1.shapesize(stretch_wid=5, stretch_len=1)
self.shapesize(stretch_wid=5, stretch_len=1)
# then we stretch to our requirements

# c. place them stacked over one another
# see above

# d. move them to the edge of the screen
block1.goto(x=350, y=0)
self.goto(x=350, y=0)

# e. be able to move the paddle with your up and down buttons
def up(self):
    self.goto(self.xcor(), self.ycor() + 20)
def down(self):
    self.goto(self.xcor(), self.ycor() + 20)
# in the Pong.py file
block1 = Paddle()
screen.listen()
block1.onkey(up, key='Up')
block1.onkey(down, key='Down')
# now remember, when you use a function as a parameter, you do not want to use parenthesis,
# if you do it will not work

# lastly, to get rid of unwanted animations
screen.tracer(0)
game_on = True
while game_on:
    screen.update()


# 199 Write the Paddle Class and Create the Second Paddle

# We have already done it, we only need to refactor the code for a separate right and left paddle
# just modify the __init__ line to take an argument, and then provide the coordinates when creating the blocks
# In the paddle.py file
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
# in the Pong.py file
block1 = Paddle((350, 0))
block2 = Paddle((-350, 0))
# Similarly to create the keybindings for the second paddle -
screen.listen()
screen.onkey(block1.up, key="Up")
screen.onkey(block1.down, key="Down")
screen.onkey(block2.up, key="w")
screen.onkey(block2.down, key="s")


# 200 Write the Ball Class and Make the Ball Move
# create a separate file, ball.py and in it create the class Ball
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

# in the Pong.py file, add the ball movement
game_on = True
while game_on:
    pong.move()
    screen.update()

# cannot see the ball moving, it flies off the screen before the screen updates
# how to enforce screen.update at 0.1 second interval?
import time
while game_on:
    time.sleep(0.1)
    # this means that before the while loop starts again the screen will sleep for 0.1 second
    # then the ball will move 20 paces, then the screen will update
    pong.move()
    screen.update()


# 201 Add the Ball Bouncing Logic

# add boundaries
# the screen is 600px tall
upper_boundary = 300
lower_boundary = -300

# detect collision with the boundaries
if pong.ycor() > 280 or pong.ycor() < -280:
    pong.bounce()

# make the ball bounce when it hits the boundaries
# whichever side the ball comes from, if it hits one of the top/bottom walls, its y coordinate reverses
# change in x will be accommodated when the ball hits the paddles
self.y_move *= -1


# 202 How to Detect Collisions with the Paddle

# The old method where we calculate distance between the two turtle objects will not work here
# Because the paddle turtle is longer, the distance looks at the center of the turtle object

# We could say that if the distance between the two turtle objects is larger, say 50 px
# That will not work too, because then, oftentimes, ball will bounce before even hitting the turtle
# Think, it is coming towards the center of the paddle, comes within 50px, then bounces back without hitting the paddle

# We can put an additional argument, if the ball come within x = 350, then we know it is within the paddle boundary

# in the ball.py file
def ricochet(self):
    self.x_move *= -1
# in the Pong.py file
game_on = True
while game_on:
    time.sleep(0.1)
    pong.move()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()
    if pong.xcor() > 320 and pong.distance(block1) < 50 or pong.xcor() < -320 and pong.distance(block2) < 50:
        pong.ricochet()
    screen.update()


# 203 How to Detect when the Ball goes Out of Bounds

# basically when the ball passes the side edges where or passes x = 380,
# then it should go back to center and advance towards the other player
# need separate if statements because later we need to do the scoring
# in the Pong.py file

    if pong.xcor() > 380:
        # get it to the original position
        pong.home()
        # it was travelling downwards, reverse it to travel upwards, otherwise it would advance the opponent downwards
        pong.bounce()
        # lastly it should move in the opposite direction
        pong.ricochet()

    if pong.xcor() < -380:
        pong.home()
        pong.bounce()
        pong.ricochet()


# 204 Score Keeping and Changing the Ball Speed

# create a new scoreboard.py file
# in there write -
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0

    def update(self):
        self.score += 1

# in the Pong.py file, add
score1 = Scoreboard()
score1.goto(0, 280)
score1.write(f'Player 1 score - {score1.score}', move=False, align='center', font=('Courier', 10, 'bold'))
score2 = Scoreboard()
score2.goto(0, -280)
score2.write(f'Player 2 score - {score1.score}', move=False, align='center', font=('Courier', 10, 'bold'))
if pong.xcor() > 380:
    pong.home()
    pong.bounce()
    pong.ricochet()
    score2.score += 1
    score2.clear()
    score2.write(f'Player 2 score - {score2.score}', move=False, align='center', font=('Courier', 10, 'bold'))

if pong.xcor() < -380:
    pong.home()
    pong.bounce()
    pong.ricochet()
    score1.score += 1
    score1.clear()
    score1.write(f'Player 1 score - {score1.score}', move=False, align='center', font=('Courier', 10, 'bold'))

# Now how to increase the speed everytime it hits the paddle?
# turtle.speed() will not work because the screen will sleep before it lets you see the changes,
# so the changes may be fast, but you will see it slower
# the trick is to tinker with the time.sleep() function

# in the ball.py file, add -
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
    def ricochet(self):
        self.x_move *= -1
        self.move_speed *= 0.9
# in the Pong.py file, add
while game_on:
    time.sleep(pong.move_speed)

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


# 205 Picturing fears_ even the worst-case scenario is not so scary
