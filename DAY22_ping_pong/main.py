from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PING PONG GAME")
screen.tracer(0)

screen.listen()

# paddle = Turtle()
# paddle.shape("square")
# paddle.shapesize()
left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_move_speed)
    screen.update()
    ball.move()

    #detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        #to bounce back
        ball.bounce_y()

    # Right paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    # Left paddle collision
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    #detect if paddle miss the ball
    #right paddle miss
    if ball.xcor() >380 :
        #reset ball to center
        ball.center()
        scoreboard.l_point()
    #left paddle miss
    if ball.xcor()<-380:
        ball.center()
        scoreboard.r_point()

screen.exitonclick()