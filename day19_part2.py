import turtle
from turtle import Turtle ,Screen
import  random


race_start = True
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make a bet red green yellow blue black orange" , prompt="make a bet which color turtle  will win ?")
print(user_bet)
y_pos = [-150,-100,-50,0,50,100]
colors = ["red", "green", "yellow", "blue", "black", "orange"]
turtle_name = []
for index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_pos[index])
    new_turtle.color(colors[index])
    turtle_name.append(new_turtle)
#print(turtle_name)
if user_bet :
    race_start = True
while race_start:
    for turt in turtle_name:
        # check who won the race
        if turt.xcor()>230:
            race_start = False
            print(turt.pencolor())
            if turt.pencolor() == user_bet:
                print(f"You won the bet the turtle color {turt.pencolor()} won the race ")
            else:
                print(f"You lost {turt.pencolor()} won the race")

        rand_distance = random.randint(0,10)
        turt.forward(rand_distance)




screen.exitonclick()


