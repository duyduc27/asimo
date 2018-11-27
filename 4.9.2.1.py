# Exercise 2 OK
import turtle
def draw_square(t , sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)



wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(3)

size = 20                   # Size of the smallest square

for n in range(5):
    draw_square(tess , size)
    tess.right(135)
    tess.penup()
    tess.forward(15)
    tess.right(-135)
    tess.pendown()
    size = size + 20
wn.exitonclick()