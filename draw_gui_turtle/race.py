from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choosen_winner = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? '
                                                                     'Enter your color : ')

colors = ['red', 'orange', 'green', 'blue', 'yellow', 'violet']
turtles = []


def new_turtles():
    y_coordinate = -120
    for the_color in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(the_color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_coordinate)
        turtles.append(new_turtle)
        y_coordinate += 50


def start_race():
    race = True
    while race:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))
            if float(turtle.xcor()) > 230.00:
                race = False
                if user_choosen_winner == turtle.color()[0]:
                    print(f'Congratiulations, {user_choosen_winner}, has won the race!!')
                else:
                    print(f'You lose, the winner is {turtle.color()[0]}')


new_turtles()
start_race()
screen.exitonclick()
