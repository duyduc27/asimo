# Exercise 5.14.1 OK
''' Make input statement with interger '''
n = int(input("Enter a number of day from 0 to 6: "))

if n >= 7 or n <0:      # Conditions error
    print("Your number is out of range!")
else:
    if n == 0:
        print("That's Sunday")
    elif n == 1:
        print("That's Monday")
    elif n == 2:
        print("That's Tuesday")
    elif n == 3:
        print("That's Wedsday")
    elif n == 4:
        print("That's Thursday")
    elif n == 5:
        print("That's Friday")
    elif n == 6:
        print("That's Saturday")