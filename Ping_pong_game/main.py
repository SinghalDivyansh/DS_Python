import time
from turtle import Screen,Turtle
from field import Field
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
position=[-400,400]
pads=[]


screen=Screen()
screen.bgcolor("black")
screen.screensize(800,600)

screen.tracer(0)
field=Field()
bal=Ball()
board1=Scoreboard(-50,250)
board2=Scoreboard(50,250)
screen.update()
for i in position:
    pad = Paddle(i)
    pads.append(pad)
screen.listen()
screen.onkey(key="w", fun=pads[0].move_up)
screen.onkey(key="s", fun=pads[0].move_down)
screen.onkey(key="Up", fun=pads[1].move_up)
screen.onkey(key="Down", fun=pads[1].move_down)
while True:
    time.sleep(0.1)
    screen.update()
    bal.ball_move()

    if bal.ycor()>300:
        bal.ball_bounce_y()
        screen.update()
    elif bal.ycor()<-300:
        bal.ball_bounce_y()
        screen.update()
    elif pads[0].distance(bal)<50 and bal.xcor()>-395:
        bal.ball_bounce_x()
        screen.update()

    elif pads[1].distance(bal)<50 and bal.xcor()<395:
        bal.ball_bounce_x()
        screen.update()
    elif bal.xcor()>450 :
        bal.setposition(0,0)
        pads[0].setposition(-400,0)
        pads[1].setposition(400, 0)
        board1.update_score()
        board1.scores()
        screen.update()
    elif bal.xcor()<-450:
        bal.setposition(0, 0)
        pads[0].setposition(-400, 0)
        pads[1].setposition(400, 0)
        board2.update_score()
        board2.scores()
        screen.update()




screen.exitonclick()