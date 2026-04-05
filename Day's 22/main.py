import time
from turtle import Screen
from paddel import Paddel
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("ping pong")
screen.bgcolor("black")
screen.tracer(0)

paddel_left = Paddel((-350,0))
paddel_right = Paddel((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddel_left.paddel_up,"w")
screen.onkey(paddel_left.paddel_down,"s")
screen.onkey(paddel_right.paddel_up,"p")
screen.onkey(paddel_right.paddel_down,"l")

is_game_over = True
while is_game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#ball will bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()
    #if ball go beyond x axis then reset
    if ball.distance(paddel_right) < 50 and ball.xcor() > 320 or ball.xcor() < -320 and ball.distance(paddel_left) < 50:
        ball.bounce_x()
# if left side miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()
    # if right side miss the ball

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()