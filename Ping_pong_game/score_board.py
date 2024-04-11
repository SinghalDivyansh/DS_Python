from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.setposition(x,y)
        self.color("white")
        self.scores()
    def scores(self):
        self.clear()
        self.write(f"{self.score}",font=("Algerian",45))
    def update_score(self):
        self.score += 1
