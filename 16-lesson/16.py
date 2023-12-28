# import another_module
# print(another_module.another)
# import turtle
# from turtle import Turtle, Screen

# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.speed(10)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable, MSWORD_FRIENDLY

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table.align)

print(table)