# Exercise 10.6.5
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
    Modify previous program then we can still realize
    the rest of lights when they turn off.
    Green, green and orange, orange, red. We number these states  0, 1, 2, 3.
    With timer like exercise requisition.
    """
    global state_num
    if state_num == 0:
        red.color("black")
        orange.color("black")
        green.color("green")
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:
        red.color("black")
        orange.color("orange")
        green.color("green")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2:
        red.color("black")
        orange.color("orange")
        green.color("black")
        state_num = 3
        wn.ontimer(advance_state_machine, 1000)
    else:
        red.color("red")
        orange.color("black")
        green.color("black") # Show up our green
        state_num = 0
        wn.ontimer(advance_state_machine, 2000)

advance_state_machine()


wn.exitonclick()
