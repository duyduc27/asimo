# Exercise 4.5.2 OK
import turtle
wn = turtle.Screen()   #Create screen and set attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  #Create turtle and set attributes
tess.color("blue")
tess.pensize(2)

k= 0

for i in range(99):     # 59 /4 lẻ 1 để có cạnh như hình cuối
    k = k +5            #Increase size each turn
    tess.right(89)
    tess.forward(k)

tess.right(90) #Relocate last turn

wn.exitonclick()