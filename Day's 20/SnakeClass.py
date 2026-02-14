from turtle import Turtle
POSITIONS = [(0,0) , (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self ):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self,position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snakes.append(snake)

    def extended_snake(self):
        self.add_snake(self.all_snakes[-1].position())


    def move_snake(self):
        for snake_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[snake_num - 1].xcor()
            new_y = self.all_snakes[snake_num - 1].ycor()
            self.all_snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)