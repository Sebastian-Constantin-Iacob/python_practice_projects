from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1

    def move(self):
        self.goto(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.bounce_x()

    def increse_velocity(self):
        self.velocity *= 0.8
