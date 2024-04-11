import time
from turtle import Turtle,Screen

import level
import obstacle
from player import Player
obst=[]
s=Screen()
s.tracer(0)
pla=Player()
obs = obstacle.Obstacle()
lev=level.Level()
s.screensize(300,300)

s.bgcolor("black")
game_on=True
while game_on:
    time.sleep(0.5)
    obs.car()
    obs.move()
    for car in obs.all_car:
        if car.distance(pla)<10:
            game=Turtle()
            game.color("white")
            game.hideturtle()
            game.write("Game Over",font=("algerian",30),align="center")
            game_on=False
    if pla.ycor()>300:
        pla.setposition(0,-300)
        lev.update()
        lev.board()

    s.update()



    s.listen()
    s.onkey(key="w", fun=pla.move_up)
    s.onkey(key="s", fun=pla.move_down)
    s.onkey(key="d", fun=pla.move_right)
    s.onkey(key="a", fun=pla.move_left)
s.update()


s.exitonclick()
