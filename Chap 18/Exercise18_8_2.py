import turtle
from math import sqrt
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
luci = turtle.Turtle()
luci.color("red")
luci.forward(200)

def Cesaro(t, order, size):
    if order == 0:
        t.forward(size) #basic case
    else:
        for angle in [-85, 170, -85, 0]:
            Cesaro(t, order -1, size/order)
            t.left(angle)

def Cesaro_square(t, order, size):
    for i in range(4):
        t.right(90)
        Cesaro(t, order, size)

#Cesaro( tess, 1, 200)
#Cesaro( tess, 2, 200)
#Cesaro( tess, 3, 200)
#Cesaro_square(tess, 1, 200)
#Cesaro_square(tess, 2, 200)
Cesaro_square(tess, 2, 50)
Cesaro_square(luci, 1, 50)
#c/ I think that the key was in line 17th, if we change to size instead of size/3
#c/ we will have a square in order 1 equals to small squares in order 2
#c/ but I have no idea what value we should put in here!
wn.exitonclick()