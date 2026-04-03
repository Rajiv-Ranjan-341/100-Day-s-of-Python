from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(800, 600)

is_race= False

user_bet = screen.textinput("Make your bet", " What would you like your bet to be?\n red', 'blue', 'green', 'yellow', 'purple', 'cyan', 'pink'")
color= ['red', 'blue', 'green', 'yellow', 'purple', 'cyan', 'pink']
y_position= [150, 100 , 50  , 0 ,  -50 , -100 , -150]
all_turtles = []
for i in range(0,7):
    tim = Turtle("turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-360,y_position[i])
    all_turtles.append(tim)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 360:
            is_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
               print(f"Race Over you win, The winner is {winning_turtle}")
            else:
                print(f"Race Over you lost, The winner is {winning_turtle}")

        distance=random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()