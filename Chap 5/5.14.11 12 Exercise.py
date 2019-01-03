#Exercise 5.14.11 12 OK
def is_rightangled():
    while True:
        a = int(input("Enter a length of a side: "))
        b = int(input("Enter a length of a side: "))
        c = int(input("Enter a length of a side: "))
        if c == (a**2 + b**2)**0.5 or b == (a**2 + c**2)**0.5 or a == (c**2 + b**2)**0.5:
            print("This is a right-angled triangle")
            break
        else:
            print("This is not a right-angled triangle. Please try again")

is_rightangled()