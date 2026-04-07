from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

    def game_over(self):
        self.write("GAME OVER" , align=ALIGNMENT, font=FONT)

    def you_win(self):
        self.write("YOU WIN" , align=ALIGNMENT, font=FONT)

