import turtle
from turtle import Turtle , Screen
import heroes
import random
print(heroes.gen())

bob = Turtle()
bob.shape("turtle")
i =0
 #draw a dashed line

# while (i<4):
#     bob.forward(50)
#     bob.penup()
#     bob.forward(50)
#     bob.pendown()
#     i+=1

#draw a dashed line
# j=0
# while (j<4):
#     bob.forward(5)
#     bob.color("white")
#     bob.forward(5)
#     bob.color("black")
#     j+=1
# draw a squre
# while (i<4):
#     bob.forward(100)
#     bob.right(90)
#     i+=1

#challenge 2 draw 10 shape sides
color = ["red","white","purple","green","yellow","brown","pink","orange","grey"]
# for i in range(3,11):
#     bob.pencolor(random.choice(color))
#     for j in range (0,i):
#         bob.forward(100)
#         bob.right(360/i)

# Random walk
move = [0,90,180,270]
bob.speed(0)
#thickness
bob.pensize(3)
# for i in range (0,100):
#     bob.pencolor(random.choice(color))
#     bob.forward(60)
#     bob.setheading(random.choice(move))

#set rgb color mode to turtle library
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colorr = (r,g,b)
    return random_colorr
# for i in range (0,100):
#     bob.pencolor(random_color())
#     bob.forward(60)
#     bob.setheading(random.choice(move))

#challenge to draw spirograph
# for i in range (0,100):
#     bob.circle(100)
#     bob.pencolor(random_color())
#     bob.setheading(random.randint(0,360))

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        bob.color(random_color())
        bob.circle(100)
        bob.setheading(bob.heading()+size_of_gap)

draw_spirograph(7)


screen = Screen()
screen.exitonclick()

