from turtle import Turtle, Screen
from random import *

is_race_on = False
screen = Screen()
screen.setup( width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtl will win the race? Enter you color vote: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
yaxis = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for n in range(0,6):
    tojen= Turtle(shape="turtle")
    tojen.color(color[n])
    tojen.penup()
    tojen.goto(x=-230, y= yaxis[n])
    all_turtles.append(tojen)

if user_bet:
    is_race_on = True
    while is_race_on:
        for turtles in all_turtles:
            if turtles.xcor() > 230:
                winning_turtle = turtles.pencolor()
                if winning_turtle == user_bet:
                    print(f"You've won! the {winning_turtle} turtle is the winner")
                else:
                    print(f"You've lost! the {winning_turtle} turtle is the winner")
                is_race_on= False

            rand_dist = randint(0, 10)
            turtles.forward(rand_dist)

screen.exitonclick()