# Exercise 7.26.11
import turtle

data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

wn = turtle.Screen() # Create turtle screen
wn.bgcolor("lightgreen") # Set turtle screen attribute

pirate = turtle.Turtle() # Create pirate turtle
pirate.color("blue") # Set turtle attribute

for (a,b) in data:
    pirate.left(a)
    pirate.forward(b)

wn.exitonclick()