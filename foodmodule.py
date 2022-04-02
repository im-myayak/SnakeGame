import random

from turtle import Turtle

EXTREMITY = 285


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        xcor = random.randint(-EXTREMITY, EXTREMITY)
        ycor = random.randint(-EXTREMITY, EXTREMITY)
        self.goto(xcor, ycor)
