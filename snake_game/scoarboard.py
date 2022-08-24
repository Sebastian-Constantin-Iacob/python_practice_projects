from turtle import Turtle
score = -1
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
COLOR = "white"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open('data.txt') as file:
            self.highscore = file.read()
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.color(COLOR)
        self.restart_score()

    # Score update
    def upd_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE = {str(self.score)}     HIGH SCORE : {self.highscore}", align=ALIGNMENT, font=FONT)

    # Get new score
    def upd_high_score(self):
        if int(self.highscore) < self.score:
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
            self.highscore = self.score

    # Restart game
    def restart_score(self):
        self.upd_high_score()
        self.score = -1
        self.upd_score()
