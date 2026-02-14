from turtle import  Screen
from SnakeClass import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
all_snakes = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "W")

screen.onkey(snake.down, "s")
screen.onkey(snake.down, "S")

screen.onkey(snake.left, "a")
screen.onkey(snake.left, "A")

screen.onkey(snake.right, "d")
screen.onkey(snake.right, "D")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
#SNAKE GONNA EAT THE FOOD
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extended_snake()
        scoreboard.increase_score()
#GAME OVER WHEN SNAKE HIT THE WALL
    if snake.head.xcor() > 395 or snake.head.xcor() < -395 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        is_game_on = False
        scoreboard.game_over()
#GAME OVER WHEN SNAKE HIT HIS TAIL
    for snake_part in snake.all_snakes[1:]:#slice in list
        if snake.head.distance(snake_part)<10:
            is_game_on = False
            scoreboard.game_over()





screen.exitonclick()