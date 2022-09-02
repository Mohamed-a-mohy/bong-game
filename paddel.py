from turtle import Turtle


class Paddel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.goto(position)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), y=new_y)



