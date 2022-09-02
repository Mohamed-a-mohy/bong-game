from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.collied = False
        self.new_x = 0.1
        self.new_y = 0.1

    def move(self):
        new_x = self.xcor()+self.new_x
        new_y = self.ycor()+self.new_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.new_y *= -1

    def paddel_collide(self):
        self.new_x *= -1

    def reset_ball(self):
        self.goto(0, 0)





