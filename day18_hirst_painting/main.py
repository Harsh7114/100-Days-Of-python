# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
# print(rgb)
import turtle
from turtle import Turtle , Screen
import random
# to use rgb color in turtle library
turtle.colormode(255)
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 234), (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132,
 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181),
(59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

bob = Turtle()
bob.pensize(20)
bob.shape("turtle")
bob.speed(0)
bob.up()
#move position from center
bob.goto((-300,-300))
bob.down()
# for i in range (0,5):
#     bob.dot(20, color_list[random.randint(0, 29)])
#     bob.penup()
#     bob.forward(30)
for i in range(0,10):
    for j in range(0,10):
        bob.dot(20,color_list[random.randint(0,29)])
        bob.penup()
        bob.forward(50)
        bob.hideturtle()
    bob.left(90)
    bob.penup()
    bob.forward(50)
    bob.left(90)
    bob.forward(500)
    bob.setheading(0)


screen =Screen()
screen.exitonclick()
