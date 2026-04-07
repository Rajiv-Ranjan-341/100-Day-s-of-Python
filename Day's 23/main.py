import time
from turtle import Screen
from scoreboard import Scoreboard
from tim_turtle import Tim_turtle
from car import Car


screen = Screen()

screen.tracer(0)
scoreboard = Scoreboard()
tim_turtle = Tim_turtle()
screen.screensize(800 ,600)

car = Car()



screen.listen()
screen.onkey(tim_turtle.go_up, key="space")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()



    for car_m in car.all_car:
        if car_m.distance(tim_turtle) < 20:
            is_game_on = False
            scoreboard.game_over()


    #when tim pass the car's
    if tim_turtle.ycor() > 280:
        tim_turtle.go_down()
        # scoreboard.you_win()
        car.increase_speed()

screen.exitonclick()