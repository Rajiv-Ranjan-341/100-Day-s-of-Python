from turtle import Turtle

class Tim_turtle(Turtle):
    def __init__(self):
        super().__init__()


        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(0,-280)


    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(0, y_cor)

    def go_down(self):
        self.goto(0, -280)
