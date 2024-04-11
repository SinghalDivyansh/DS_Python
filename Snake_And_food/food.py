import random,turtle
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh_food()
        self.shape("circle")
        self.shapesize(0.4)
        self.color("blue")
        self.penup()


    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.setposition(random_x, random_y)
