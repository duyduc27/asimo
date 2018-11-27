# Exercise 2 tam OK
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
    k = (2*(size/2)**2)**0.5
    tess.right(135)
    tess.penup()
    tess.forward(k)
    tess.right(-135)
    tess.pendown()
    size = size + size
wn.exitonclick()