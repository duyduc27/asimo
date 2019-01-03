# Exercise 10.6.3
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
green = turtle.Turtle() # Create 3 turtles correspond with 3 traffic lights
orange = turtle.Turtle()
red = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    green.pensize(3)
    green.color("black", "darkgrey")
    green.begin_fill()
    green.forward(80)
    green.left(90)
    green.forward(200)
    green.circle(40, 180)
    green.forward(200)
    green.left(90)
    green.end_fill()

draw_housing()

green.penup()
# Position "green" onto the place where the green light should be
green.forward(40)
green.left(90)
green.forward(50)
# Turn "green" into a big green circle
green.shape("circle")
green.shapesize(3)
green.fillcolor("green")

a = green.position() # We get them to the same position
orange.goto(a)
red.goto(a)

orange.left(90) # Turn "orange" into a big orange circle
orange.forward(70)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("orange")

red.left(90) # Turn "red" into a big red circle
red.forward(140)
red.shape("circle")
red.shapesize(3)
red.fillcolor("red")

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    """
    Orange, Red, Green.  We number these states  0, 1, 2. With timer
    red for 10 seconds, orange for 3 seconds and green for 10 seconds
    """
    global state_num
    if state_num == 0:
        red.hideturtle()
        orange.showturtle() # Show up our orange
        green.hideturtle()
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:
        red.showturtle() # Show up our red
        orange.hideturtle()
        green.hideturtle()
        state_num = 2
        wn.ontimer(advance_state_machine, 10000)
    else:
        red.hideturtle()
        orange.hideturtle()
        green.showturtle() # Show up our green
        state_num = 0
        wn.ontimer(advance_state_machine, 10000)

advance_state_machine()

""" In program, the way with one turtle (10.6.2) is definitely faster
and more comfortable than the rest one. But in reality, we used all of 3 lights
take turns doing traffic light work. So the rest one (with 3 turtles - 10.6.3)
is more closely resembles reality"""

wn.exitonclick()
