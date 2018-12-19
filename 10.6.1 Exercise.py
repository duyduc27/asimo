# Exercise 10.6.1

import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

""" First of all, we set initial value of turtle pensize
    With her default value equals one
"""
n = 1

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def h5():                           # Create handler 5,6,7 for turtle color
    tess.color("red")

def h6():
    tess.color("green")

def h7():
    tess.color("blue")

def h8():   # Use keypress to increase pensize
    global n
    n += 1
    if 1 <= n <= 20:    # Condition to set limit of turtle pensize
        tess.pensize(+ n)


def h9():  # Use keypress to decrease pensize
    global n
    n -= 1
    if n < 1: # Set this condition for minimum pensize value is always 1 !
        n = 1
    elif 1 <= n <= 20:
        tess.pensize(n)

def h10(): # Use keypress to change window size
    """ Note: screen size method only support for positive integer"""
    x = int(input("width?"))
    y = int(input("height?"))
    turtle.screensize(x, y)
    wn.title(("Your window size is {0} x {1}").format(x, y))

def h11(): # Use keypress to change turtle attributes
    tess.shape("turtle")


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(h8, "+")
wn.onkey(h9, "-")
wn.onkey(h10, "c")
wn.onkey(h11, "t")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()