from turtle import Turtle
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align='center', font=FONT)
