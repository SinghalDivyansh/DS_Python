import random
from turtle import Turtle,Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=10
        self.y=10
    def ball_move(self):
        self.setheading(random.randint(0,360))
        self.goto(self.xcor()+self.x,self.ycor()+self.y)
    def ball_bounce_y(self):
        self.y*=-1
    def ball_bounce_x(self):
        self.x*=-1