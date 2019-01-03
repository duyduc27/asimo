#Exercise 5.14. 7 8 9
import turtle
xs = [-48, 117, -200, 240, 160, 260, 220]

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    """ Idea: draw 2/3 of 'Invisible' rectangle then use it for printing
    negative data value at bottom bar (forward -15 units),
    then turn back into normal chart like nothing happend"""
    t.begin_fill()        # Fill color in column
    t.left(90)
    t.forward(height)     # Draw up the left side
    if height >= 0 :
        t.write('  ' + str(height))  # Write values at top of column
        t.right(90)
        t.forward(40)         # Width of bar, along the top
        t.right(90)
        t.forward(height)     # And down again!
        t.left(90)            # Put the turtle facing the way we found it.
        t.end_fill()
        t.penup()             # Remove the gap between columns
        t.forward(10)         # Leave small gap after each bar
        t.pendown()
    else:
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.end_fill()
        t.penup()
        t.forward(-(height-15))
        t.right(90)
        t.forward(40)
        t.right(180)
        t.write('  ' + str(height))
        t.forward(40)
        t.right(90)
        t.forward(height-15)
        t.left(90)
        t.forward(10)         # Leave small gap after each bar
        t.pendown()

wn = turtle.Screen()    # Create turtle Screen
wn.bgcolor("lightgreen") # Set attribute Screen

tess = turtle.Turtle() # Create turtle
tess.pensize(3)         # Set attribute turtle

for v in xs:
    if v >= 200:
        tess.color("blue", "red")
    elif 100 <= v < 200:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")
    draw_bar(tess, v)       # Assume xs and tess are ready

wn.exitonclick()