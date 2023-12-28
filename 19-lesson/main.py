import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.forward(-10)

def rotate_counter_clockwise():
    current_heading = tim.heading() + 5
    tim.setheading(current_heading)

def rotate_clockwise():
    current_heading = tim.heading() - 5
    tim.setheading(current_heading)

def clean_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clean_screen)

screen.exitonclick()