from turtle import Turtle, Screen


bob = Turtle()
screen = Screen()
def move_forward():
    bob.forward(50)
def move_backward():
    bob.backward(50)
def counter_clock():
    #bob.left(20)
    new_heading = bob.heading() - 10
    bob.setheading(new_heading)

def clockwise():
    #bob.right(20)  or using heading
    new_heading = bob.heading()+10
    bob.setheading(new_heading)
def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=counter_clock)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()