from turtle import Screen
from paddel import Paddel
from ball import  Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)
r_paddel = Paddel((350, 0))
l_paddel = Paddel((-350, 0))

screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")

ball = Ball()
game_on = True

score = Score()

while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddel) < 50 and ball.xcor() > 330) or (ball.distance(l_paddel) < 50 and ball.xcor() < -330):
        print("ayy")
        ball.paddel_collide()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.score_edit("l")

    if ball.xcor() < -380:
        ball.reset_ball()
        score.score_edit("r")


screen.exitonclick()


