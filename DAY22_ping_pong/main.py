from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PING PONG GAME")

screen.listen()

# paddle = Turtle()
# paddle.shape("square")
# paddle.shapesize()
left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()

