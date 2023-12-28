import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will winn the race? Enter a color: ")
colors = ['red', "orange", "yellow", "green", "blue", "purple"]
y_position = -150
all_turtles = []

for turtle_index in range(0, len(colors)):
    new_turtle = colors[turtle_index]
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-270, y=y_position)
    y_position += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You're WON! The {winning_color} turtle is the winner!")
            else:
                print(f"You're Lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()