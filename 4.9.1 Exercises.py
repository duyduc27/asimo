# Exercise 1 OK
def draw_square():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("hotpink")
    alex.pensize(2)

    for n in range(4):
        for i in range(4):
            alex.forward(20)
            alex.left(90)
        alex.penup()
        alex.forward(40)
        alex.pendown()


    wn.exitonclick()

draw_square()


