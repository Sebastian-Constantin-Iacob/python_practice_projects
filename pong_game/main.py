from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

game_on = True

screen = Screen()
screen.tracer(0)

paddle_left = Paddle('left')
paddle_right = Paddle('right')
ball = Ball()
scorebord = ScoreBoard()


def initialize_screen():
    screen.bgcolor("black")
    screen.title("The Pong Game")
    screen.setup(width=800, height=600)


screen.listen()
screen.onkey(paddle_right.go_up, 'Up')
screen.onkey(paddle_right.go_down, 'Down')
screen.onkey(paddle_left.go_up, 'w')
screen.onkey(paddle_left.go_down, 's')

initialize_screen()

while game_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    # Detect colision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect colision with the paddles
    if (ball.distance(paddle_left) < 50 and ball.xcor() < -320) or (ball.distance(paddle_right) < 50 and ball.xcor()
                                                                    > 320):
        ball.bounce_x()
        ball.increse_velocity()

    # Right scores
    if ball.xcor() < -380:
        ball.restart()
        scorebord.score_increse_right()

    # Left scores
    if ball.xcor() > 380:
        ball.restart()
        scorebord.score_increse_left()

screen.exitonclick()
