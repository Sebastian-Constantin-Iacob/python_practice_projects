from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,side):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == 'left':
            self.goto(x=-350, y=0)
        else:
            self.goto(x=350, y=0)


    def go_up(self):
        if self.ycor() < 250:
            self.goto(x=self.xcor(), y=(self.ycor() + 20))

    def go_down(self):
        if self.ycor() > -250:
            self.goto(x=self.xcor(), y=(self.ycor() - 20))
