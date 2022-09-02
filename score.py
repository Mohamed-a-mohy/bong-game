from turtle import Turtle

lscore = 0
rscore = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.ht()
        self.write(f"Score = {lscore}  |  {rscore}", False, align="center")


    def score_edit(self, side):
        global rscore
        global lscore

        if side == "l":
            lscore += 1

        if side == "r":
            rscore += 1
        self.clear()
        self.write(f"Score = {lscore}  |  {rscore}", False, align="center")

