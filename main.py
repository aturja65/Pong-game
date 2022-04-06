from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
left = 0
right = 0
game = True
while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if l_paddle.distance(ball) < 50 and ball.xcor() < -320 or r_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.xcor() > 350:
        ball.reset_position()
        left = scoreboard.l_point()
    elif ball.xcor() < -350:
        ball.reset_position()
        right = scoreboard.r_point()

    if left == 5 or right == 5:
        game = False
        scoreboard.game_over()
screen.exitonclick()
