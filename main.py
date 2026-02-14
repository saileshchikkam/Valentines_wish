from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("#ffe6f0")
screen.title("Valentine Wish")

t = Turtle()
# t.hideturtle()
t.shape("turtle")
t.speed(3)
t.pensize(3)
t.color("#ff1a66")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.hideturtle()
t.end_fill()

text = Turtle()
text.hideturtle()
text.penup()
text.goto(0, -80)  # for height adjustment
text.color("#800040")

text.write("Happy  Valentine's  Day",
           align="center",
           font=("Comic Sans MS", 30, "bold"))

small = Turtle()
small.hideturtle()
small.speed(0)
small.color("#ff4d88")
# a simple function for small hearts around big hearts
def small_heart(x, y, size):
    small.penup()
    small.goto(x, y)
    small.setheading(0)
    small.pendown()
    small.begin_fill()
    small.left(140)
    small.forward(size)
    small.circle(-size / 2, 200)
    small.left(120)
    small.circle(-size / 2, 200)
    small.forward(size)
    small.end_fill()
    small.setheading(0)

small_heart(-250, 200, 40)
small_heart(250, 200, 40)
small_heart(-300, 0, 35)
small_heart(300, 0, 35)
small_heart(-250, -200, 40)
small_heart(250, -200, 40)

screen.mainloop()
