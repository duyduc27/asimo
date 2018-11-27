# 4.9.3 ok
import turtle
def draw_poly(t, n, sz):
    for i in range(n):

        t.forward(sz)
        t.left(45)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(1)

draw_poly(tess, 8, 50)

wn.exitonclick()