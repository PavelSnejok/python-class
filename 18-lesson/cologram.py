# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

color_list =[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")
tim.speed("fast")

def drawing(x, y, angle, x_dots, y_dots):
    tim.penup()
    tim.setheading(angle)
    for height in range(y_dots):
        tim.setx(x)
        tim.sety(y)
        y += 50
        for width in range(x_dots):
            tim.dot(20,random.choice(color_list))
            if width == 9:
                break
            else:
                tim.forward(50)

drawing(-225,-225, 0, 10, 10)

screen = t.Screen()
screen.exitonclick()