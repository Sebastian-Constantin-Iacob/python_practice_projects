from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car import Car
import time
import random

# Variable initializations
game_on = True
cars = []

# Screen object initialization
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Safe cross')

# Scoreboard object initialization
scoreboard = ScoreBoard()

# Player object initialization
player = Player()

# Actions based on keys pressed
screen.listen()
screen.onkey(player.move_forward, 'Up')

# Game is on
while game_on:
    # Populate cars with a new car object from the class Cars()
    if random.randint(1, 10) % 3 == 0:
        cars.append(Car())
    time.sleep(player.velocity)
    screen.update()
    for a_car in cars:
        a_car.move_car()
        if a_car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        scoreboard.increse_score()
        player.go_to_start()

screen.exitonclick()
