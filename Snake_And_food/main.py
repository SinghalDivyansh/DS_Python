
import time
import turtle
from score_board import Scoreboard


from food import Food
from turtle import Screen,Turtle
from snake import Snake
screen=Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("The Snake Game")
screen.tracer(0)
snake = Snake()
print(screen.screensize())
screen.update()
game_on=True

food=Food()
board=Scoreboard()
while game_on:
    time.sleep(0.15)
    screen.update()
    snake.move_snake()
    screen.listen()
    screen.onkey(key="Up",fun=snake.turn_up)
    screen.onkey(key="Down", fun=snake.turn_down)
    screen.onkey(key="Left", fun=snake.turn_left)
    screen.onkey(key="Right", fun=snake.turn_right)

    if snake.head.distance(food) < 20:
        food.refresh_food()
        screen.tracer(0)
        snake.add_tail()
        screen.tracer(0)
        board.score_new()

    if snake.head.xcor()>340 or snake.head.xcor()<(-340) or snake.head.ycor()>320 or snake.head.ycor()<(-320):
        board.reset()
        board.score_new()
        snake.reset()



    for seg in snake.turtle_list:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg)<10:
            board.reset()
            board.score_new()
            snake.reset()

screen.exitonclick()