from turtle import Turtle
FONT = ('Arial', 30, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-270, y=250)
        self.level_number = 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level {self.level_number}", align='left', font=FONT)

    def increse_score(self):
        self.level_number += 1
        self.update()

    def game_over(self):
        self.goto(-80, 0)
        self.write(arg=f"GAME OVER", align='left', font=FONT)
