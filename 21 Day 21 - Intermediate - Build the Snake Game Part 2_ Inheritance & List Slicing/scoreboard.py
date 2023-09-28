from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')
# this way if I want to change font I do not have to do it numerous times in code body


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.pendown()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
