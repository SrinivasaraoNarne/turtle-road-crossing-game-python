from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.scoring()

    def scoring(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def inc_score(self):
        self.score += 1
