from turtle import Turtle,Screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setposition(0, -300)
        self.color("green")

    def move_up(self):
        self.forward(10)
        Screen().update()


    def move_down(self):

        self.backward(10)
        Screen().update()

    def move_right(self):
        self.setposition(self.xcor()+10,self.ycor())
        Screen().update()

    def move_left(self):
        self.setposition(self.xcor() - 10, self.ycor())
        Screen().update()

