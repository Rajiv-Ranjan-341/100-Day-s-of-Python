from turtle import Turtle

class Paddel(Turtle):

    def __init__(self,position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)


    def paddel_down(self):
        y_cord = self.ycor() - 40
        self.goto(self.xcor(), y_cord)

    def paddel_up(self):
        y_cord = self.ycor() + 40
        self.goto(self.xcor(), y_cord)



