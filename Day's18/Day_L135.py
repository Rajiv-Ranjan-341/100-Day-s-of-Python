import turtle

import turtle as t
import random

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple
tim = t.Turtle()
tim.speed(100)

def draw(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size)

draw(5)


screen = t.Screen()
screen.exitonclick()