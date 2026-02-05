from turtle import Turtle ,Screen
import random

colours = ['red', 'blue', 'green', 'yellow', 'cyan', 'purple', 'pink']
tim = Turtle()
tim.pensize(10)
tim.speed(5)

dic = [0, 90, 180, 270]
for _ in range(100):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(dic))

screen = Screen()
screen.exitonclick()