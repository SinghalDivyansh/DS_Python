from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.penup()
        self.color("pink")
        self.goto(-50,280)
        self.extract_highscore()

        self.write(f"score:{self.score} High Score: {self.high_score}", font=("algerian", 24),align="center")

    def update_score(self):
        self.write(f"score:{self.score} High Score: {self.high_score}", font=("algerian", 24), align="center")
    def score_new(self):
        self.score+=1
        self.clear()
        self.write(f"score:{self.score} High Score: {self.high_score}", font=("algerian", 24),align="center")
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            self.rewrite_highscore()
        self.score=-1
        self.update_score()
    def extract_highscore(self):
        with open("high.txt",mode="r") as file:
            hs=int(file.read())
            self.high_score=hs
    def rewrite_highscore(self):
            with open("high.txt", mode="w") as file:
                file.write(str(self.score))

