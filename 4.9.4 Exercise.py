# Exercise 4.4 OK
import turtle
wn = turtle.Screen()   #Create screen and set attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  #Create turtle and set attributes
tess.color("blue")
tess.pensize(2)

for n in range(20):
    tess.left(18)       #Turn angle 18 degrees
    for i in range(4):  #Make square
        tess.forward(100)
        tess.left(90)


wn.exitonclick()