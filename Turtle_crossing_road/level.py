from turtle import Turtle
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(-280,280)
        self.level=1
        self.board()
    def board(self):
        self.write(f"level:{self.level}",font=("arial",16))
    def update(self):
        self.clear()
        self.level+=1