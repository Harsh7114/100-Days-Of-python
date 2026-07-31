from turtle import  Turtle , Screen
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My Snake Game ")
#to turn off screen parts deleay
screen.tracer(0)

#create a snake
dist = [0,-20,-40]
snake_3parts = []
for index in range(0,3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=dist[index],y=0)
    snake_3parts.append(new_turtle)




game_on = True
while game_on:
    # refresh the screen with help of update method
    screen.update()
    # to slow down the speed of snake parts to move
    time.sleep(0.5)
    for parts in range(start=2 , stop=0, step=-1)  #to move the parts in 3,2,1 order














screen.exitonclick()