# Exercise 4.9.6 OK
import turtle
def draw_poly(t, n, sz):
    for i in range(n):

        t.forward(sz)
        t.left(120)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(1)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

draw_equitriangle(tess, 50)

wn.exitonclick()