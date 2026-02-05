from turtle import Turtle ,Screen
import random

colours = ['red', 'blue', 'green', 'yellow', 'cyan', 'purple', 'pink']
tim = Turtle()

def draw(side_no):
    angle= 360/side_no
    for i in range(side_no):
        tim.forward(100)
        tim.left(angle)

for shape in range(3 ,11):
    tim.color(random.choice(colours))
    draw(shape)

screen = Screen()
screen.exitonclick()