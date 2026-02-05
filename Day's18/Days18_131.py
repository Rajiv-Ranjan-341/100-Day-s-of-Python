from turtle import Turtle ,Screen

t = Turtle()

# for i in range(25):
#     for color in ['black', 'white']:
#         t.color(color)
#         t.forward(5)

for _ in range(50):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen = Screen()
screen.exitonclick()