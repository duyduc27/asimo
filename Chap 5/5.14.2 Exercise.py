# Exercise 5.14.2
l = int(input("Enter a starting day number: "))
m = int(input("Enter the length of your stay: "))

n = (l + m) % 7
if l >= 7 or l <0:      # Conditions error
    print("Your day number is out of range!")

if n == 0:
    print("You come home at Sunday")
elif n == 1:
    print("You come home at Monday")
elif n == 2:
    print("You come home at Tuesday")
elif n == 3:
    print("You come home at Wedsday")
elif n == 4:
    print("You come home at Thursday")
elif n == 5:
    print("You come home at Friday")
elif n == 6:
    print("You come home at Saturday")
