from turtle import Turtle

BORDER = [(-280, -280), (-280, 280), (280, 280), (280, -280), (-280, -280)]

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(BORDER[0])
        for coordinate in BORDER:
            self.pendown()
            self.goto(coordinate)
