from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,loc):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.setposition(loc, 0)

    def move_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def move_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)


