from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')
# this way if I want to change font I do not have to do it numerous times in code body


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as datafile:
            self.high_score = int(datafile.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(220, 280)
        self.write(f"Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(220, 280)
        self.write(f"Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as datafile:
                datafile.write(f"{self.score}")
        self.refresh()
        self.home()
        self.pendown()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
