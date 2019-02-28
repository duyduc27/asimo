import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")


def Sierpinski(t, order, size):
    if order == 0:
        for angle in range(3): # basic case
            t.forward(size)
            t.left(120)
    else:
        Sierpinski(t, order -1, size/2)
        t.forward(size/2)
        Sierpinski(t, order -1, size/2)
        t.back(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        Sierpinski(t, order -1, size/2)
        t.left(60)
        t.back(size/2)
        t.right(60)


Sierpinski(tess, 3, 100)

wn.exitonclick()