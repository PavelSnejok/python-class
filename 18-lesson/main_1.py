import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(1, 255)
    b = random.randint(1, 255)
    g = random.randint(1, 255)
    color_tuple = (r, g, b)
    return color_tuple

tim.shape("turtle")
tim.speed("fastest")

n = 1
while n < 100:
    tim.pencolor(random_color())
    tim.width(10)
    tim.forward(20)
    list_turn = [0, 90, 180, 270]
    turn = random.choice(list_turn)
    tim.setheading(turn)
    n += 1

screen = t.Screen()
screen.exitonclick()