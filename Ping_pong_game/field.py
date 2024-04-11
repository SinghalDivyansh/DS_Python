from turtle import Turtle,Screen
class Field:
    def __init__(self):
        self.centre_line()
    def centre_line(self):

        t = Turtle()
        t.color("white")
        t.setheading(90)
        for i in range(20):
            t.forward(10)
            t.penup()
            t.forward(10)
            t.pendown()
        t = Turtle()
        t.color("white")
        t.setheading(270)
        for i in range(20):
            t.forward(10)
            t.penup()
            t.forward(10)
            t.pendown()
