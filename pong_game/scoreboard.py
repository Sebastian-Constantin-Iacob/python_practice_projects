from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(str(self.score_l), align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(str(self.score_r), align=ALIGNMENT, font=FONT)

    def score_increse_left(self):
        self.score_l += 1
        self.update()

    def score_increse_right(self):
        self.score_r += 1
        self.update()
