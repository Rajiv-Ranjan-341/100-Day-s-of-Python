import random
from turtle import Turtle
STRAING_MOVE =5
COLOUR = ["red","blue","green","yellow","cyan","magenta","pink"]

class Car:
    def __init__(self):
        self.all_car = []
        self.speed = STRAING_MOVE

    def create_car(self):
        random_num = random.randint(1,4)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1,3)
            new_car.penup()
            random_y = random.randrange(-200,250)
            new_car.goto(400,random_y)
            new_car.color(random.choice(COLOUR) )
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += STRAING_MOVE
