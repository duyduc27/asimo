# Exercise 5.14.10 OK
def find_hypot():
    a = int(input("Enter a length of a side: "))
    b = int(input("Enter a length of a side: "))
    c = (a**2 + b**2)**0.5

    print("Length of the hypotenuse of this triangle is:", c)

find_hypot()