from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(x=0, y=-270)
        self.left(90)
        self.velocity = 0.2

    def move_forward(self):
        self.forward(distance=10)

    def go_to_start(self):
        self.velocity *= 0.8
        self.goto(x=0, y=-270)
