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
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def inc_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as file:
                file.write(f"\n{self.high_score}")
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(GAME_OVER_POSITION)
    #     self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
