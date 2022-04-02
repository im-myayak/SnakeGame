from turtle import Turtle

SCORE_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
GAME_OVER_POSITION = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.pencolor("white")
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.score = 0
        self.display_score()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)
