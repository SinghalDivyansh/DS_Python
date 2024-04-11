from turtle import Turtle,Screen
import time

import food


class Snake:
    def __init__(self):
        self.turtle_list=[]
        self.make_snake()
        self.head = self.turtle_list[0]


    def make_snake(self):
        x=0
        for i in range(0, 3):
            tom = Turtle(shape="square")
            tom.color("white")
            tom.penup()
            tom.setx(x)
            tom.sety(0)
            x -= 20
            self.turtle_list.append(tom)
    def add_tail(self):

        tom = Turtle(shape="square")
        tom.penup()
        self.turtle_list.append(tom)
        tom.speed("fastest")
        tom.color("white")
        tom.penup()
    def reset(self):
        for seg in self.turtle_list:
            seg.goto(2000,2000)
        self.turtle_list.clear()
        self.make_snake()
        self.head = self.turtle_list[0]




    def move_snake(self):
        for turtle_num in range(len(self.turtle_list)-1, 0, -1):
            new_x = self.turtle_list[turtle_num-1].xcor()
            new_y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(new_x, new_y)
        self.turtle_list[0].forward(20)

    def turn_left(self):
        self.turtle_list[0].setheading(180)

    def turn_right(self):
        self.turtle_list[0].setheading(0)

    def turn_up(self):
        self.turtle_list[0].setheading(90)

    def turn_down(self):
        self.turtle_list[0].setheading(270)
