import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()


def turtle_forward():
    timmy.forward(10)


def turtle_backwards():
    timmy.backward(10)


def turtle_left():
    timmy.left(10)


def turtle_right():
    timmy.right(10)


def turtle_clear():
    screen.reset()
    timmy.goto(0, 0)


screen.listen()
screen.onkey(key='w', fun=turtle_forward)
screen.onkey(key='s', fun=turtle_backwards)
screen.onkey(key='a', fun=turtle_left)
screen.onkey(key='d', fun=turtle_right)
screen.onkey(key='c', fun=turtle_clear)
screen.exitonclick()