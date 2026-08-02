from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game ")
#to turn off the screen parts delay
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    # refresh the screen with help of update method
    screen.update()
    # to slow down the speed of snake parts to move
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
