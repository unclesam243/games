from turtle import Turtle, Screen  # WE need to import the dependencies so we can use them

Straw = Turtle() #We create the turtle instance
screen = Screen() #we create the screen on which it will appear

def move_w():
    w = Straw.fd(10)


fun = move_w
screen.onkey(fun, key="w")


def move_s():
    s = Straw.bk(10)


fun = move_s
screen.onkey(fun, key="s")


def move_a():
    a = Straw.left(10)


fun = move_a
screen.onkey(fun, key="a")


def move_d():
    d = Straw.right(10)


fun = move_d
screen.onkey(fun, key="d")


def clearing():
    Straw.clear()
    Straw.penup()
    Straw.home()
    Straw.pendown()

fun = clearing
screen.onkey(fun, key="c")




screen.listen()


screen.exitonclick()