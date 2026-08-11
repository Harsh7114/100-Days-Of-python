from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game ")
#to turn off the screen parts delay
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
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

    #detect collision with food using distance  method to check if two turtle collid or not
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        score.increase_score()
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
    #Detect collision with tail.
    for parts in snake.snake_3parts[1:]:
        # if parts == snake.head:
        #     pass
        if snake.head.distance(parts)<10:
            score.reset()
            snake.reset()
    #if head collid with any part ub the tail:
            #trigger game over

screen.exitonclick()
