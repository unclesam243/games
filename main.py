from turtle import Turtle, Screen

franklin = Turtle()
screen = Screen()

def move_forwar():
    franklin.forward(10)


screen.onkey(move_forwar, "space")
screen.listen()


screen.exitonclick()