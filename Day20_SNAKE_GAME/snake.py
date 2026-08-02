from turtle import Turtle
DIST = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN = 270
LEFT=180
RIGHT=0
class Snake:
    # create a snake
    def __init__(self):
        self.snake_3parts=[]
        self.create_snake()
        #set head
        self.head = self.snake_3parts[0]


    def create_snake(self):
        for index in DIST:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(index)
            self.snake_3parts.append(new_turtle)
    def move(self):
        # to move the parts in 3,2,1 order
        for parts in range(len(self.snake_3parts) - 1, 0, -1):
            new_x = self.snake_3parts[parts - 1].xcor()
            new_y = self.snake_3parts[parts - 1].ycor()
            self.snake_3parts[parts].goto(new_x, new_y)
        self.snake_3parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_3parts[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_3parts[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_3parts[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.snake_3parts[0].setheading(RIGHT)