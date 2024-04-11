import random
from turtle import Turtle
class Obstacle():
    def __init__(self):
        self.all_car=[]
    def car(self):
        t=Turtle()
        t.shape("square")
        t.penup()
        t.color("white")
        t.setposition(300,random.randint(-300,300))
        t.shapesize(stretch_wid=1,stretch_len=2)
        t.color(random.choice(["red","blue","green","purple","yellow","cyan"]))
        self.all_car.append(t)


    def move(self):
        for i in self.all_car:
            i.backward(30)