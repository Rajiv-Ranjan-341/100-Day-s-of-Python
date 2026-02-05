from turtle import Turtle , Screen

def square():
    for i in range(4):
        the_cat.forward(100)
        the_cat.left(90)

the_cat = Turtle()
the_cat.shape('turtle')
the_cat.color('red')


square()

# the_cat.left(120)
# the_cat.forward(100)
#
# print(the_cat.pos())

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         the_cat.color(c)
#         the_cat.forward(steps)
#         the_cat.right(30)

the_cat.color('red')
the_cat.fillcolor('yellow')

screen = Screen()
screen.bgcolor('black')
screen.exitonclick()

