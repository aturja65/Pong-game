from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score()

    def score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Arial", 16, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Arial", 16, "normal"))

    def l_point(self):
        self.l_score += 1
        self.score()
        return self.l_score

    def r_point(self):
        self.r_score += 1
        self.score()
        return self.r_score

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
