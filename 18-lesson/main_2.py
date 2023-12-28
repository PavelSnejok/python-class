import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.speed("fastest")

def random_color():
    r = random.randint(1, 255)
    b = random.randint(1, 255)
    g = random.randint(1, 255)
    color_tuple = (r, b, g)
    return color_tuple

def draw_spirograf(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

draw_spirograf(5)

screen = t.Screen()
screen.exitonclick()