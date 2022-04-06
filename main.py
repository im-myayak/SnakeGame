import time

from turtle import Screen
from foodmodule import Food
from scoreboard import Scoreboard
from snakemodule import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


theSnake = Snake()
theFood = Food()
theScore = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=theSnake.up)
screen.onkey(key="Left", fun=theSnake.left)
screen.onkey(key="Right", fun=theSnake.right)
screen.onkey(key="Down", fun=theSnake.down)

game_started = True

while game_started:
    screen.update()

    time.sleep(0.1)
    if theSnake.stop_condition():
        # game_started = False
        theScore.reset_score()
        theSnake.reset_the_snake()

    theSnake.move_snake()

    if theSnake.head.distance(theFood) < 15:
        theFood.move_food()
        theScore.inc_score()
        position = theSnake.tail.position()
        theSnake.new_square(position)

# Snake_Game()

screen.exitonclick()
