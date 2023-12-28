from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")

def draw_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        tim.forward(100)
        tim.right(angle)

for number_of_shapes in range(3, 11):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor((r, g, b))
    draw_shape(number_of_shapes)

screen.exitonclick()




