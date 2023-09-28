from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        # whichever side the ball comes from, if it hits one of the top/bottom walls, its y coordinate reverses
        # change in x will be accommodated when the ball hits the paddles
        self.y_move *= -1

    def ricochet(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    # def increase_speed(self):
    #     self.speed += 1
