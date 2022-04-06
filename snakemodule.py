from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOST_LEFT = -285
MOST_RIGHT = 285
MOST_DOWN = -285
MOST_UP = 285


class Snake:
    def __init__(self):
        self.list_square = []
        self.create_snake()
        self.head = self.list_square[0]
        self.tail = self.list_square[len(self.list_square)-1]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.new_square(position)

    def move_snake(self):
        for i in range(len(self.list_square) - 1, 0, -1):
            xcor = self.list_square[i - 1].xcor()
            ycor = self.list_square[i - 1].ycor()
            self.list_square[i].goto(xcor, ycor)
        self.head.forward(MOVING_DISTANCE)

    def new_square(self, position):
        new_object = Turtle(shape="square")
        new_object.up()
        new_object.color("white")
        new_object.goto(position)
        new_object.speed("fastest")
        self.list_square.append(new_object)
        self.tail = new_object

    def touch_to_itself(self):
        for obj in self.list_square[1:]:
            if self.head.distance(obj) < 15:
                return True
        return False

    def reset_the_snake(self):
        for obj in self.list_square:
            obj.goto(1000, 1000)
        self.list_square.clear()
        self.create_snake()
        self.head = self.list_square[0]
        self.tail = self.list_square[len(self.list_square) - 1]

    def stop_condition(self):
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if MOST_RIGHT < xcor or MOST_LEFT > xcor or MOST_DOWN > ycor or ycor > MOST_UP or self.touch_to_itself():
            return True
        else:

            return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
