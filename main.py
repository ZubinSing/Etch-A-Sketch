from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_back():
    tim.setheading(180)
def postioning():
    tim.penup()
def pdown():
    tim.pendown()
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward, key= "w")
screen.onkey(fun=turn_left, key= "a")
screen.onkey(fun=turn_right, key= "d")
screen.onkey(fun=move_back, key= "s")
screen.onkey(fun=postioning, key= "space")
screen.onkey(fun=pdown, key= "f")
screen.onkey(fun=clear, key= "c")


screen.exitonclick()
