#Exercise 4.9.9 OK
import turtle
# Exercise 4.9.10 OK
wn = turtle.Screen()   #Create turtle Screen
wn.bgcolor("lightgreen") #Set turtle Screen attribute

tess = turtle.Turtle() # Create turtle
tess.color("hotpink")      # Set turtle attributes
tess.pensize(3)

def draw_star():  #Void function "draw star"
    for i in range(5):
        tess.forward(100)
        tess.right(144)

for i in range(5):
    draw_star()
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

wn.exitonclick()