from turtle import Turtle
ALIGNMENT="center"
FONT = ("Courier",24,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER",font=("Courier",24,"bold"),align="center")