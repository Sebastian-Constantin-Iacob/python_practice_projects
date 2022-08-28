from turtle import Turtle
import random
car_colors = ['orange', 'red', 'blue', 'green', 'yellow']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.left(180)
        self.color(random.choice(car_colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=300, y=random.randint(-260, 260))

    def move_car(self):
        self.forward(distance=10)
