from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800 ,height=600)
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()

scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_is_on=True




while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()

    #r_paddle misses
    if ball.xcor()>380:
        scoreboard.l_point()
        ball.reset()

    #l_paddle misses
    if ball.xcor()<-380:
        scoreboard.r_point()
        ball.reset()

    if(scoreboard.l_score==10):
        game_is_on=False
        scoreboard.gameWinner("Left")

    if(scoreboard.r_score==10):
        game_is_on=False
        scoreboard.gameWinner("Right")

    



screen.exitonclick()