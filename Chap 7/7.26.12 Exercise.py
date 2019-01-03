# Exercise 7.26.12
import turtle

data = [
(0, 40), (90, 40), (90, 40), (90, 40),
(135, 3200**0.5), (90, 30), (90, 30), (90, 3200**0.5)
]
"""The data set up for drawing turtle.
The lines didn't go over more than once and not lifing the pen"""

wn = turtle.Screen() # Create turtle screen
wn.bgcolor("lightgreen") # Set turtle screen attribute

pirate = turtle.Turtle() # Create pirate turtle
pirate.color("blue") # Set turtle attribute
pirate.pensize(3)

for (a,b) in data:
    pirate.left(a)
    pirate.forward(b)

wn.exitonclick()