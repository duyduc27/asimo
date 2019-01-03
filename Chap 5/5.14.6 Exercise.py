#Exercise 5.14.6 OK
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, \
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    if i >= 75:
        print("Your mark is", i, "So you have been graded First")
    elif 70 <= i < 75:
        print("Your mark is", i, "So you have been graded Upper Second")
    elif 60 <= i < 70:
        print("Your mark is", i, "So you have been graded Second")
    elif 50 <= i < 60:
        print("Your mark is", i, "So you have been graded Third")
    elif 45 <= i < 50:
        print("Your mark is", i, "So you have been graded F1 Supp")
    elif 40 <= i < 45:
        print("Your mark is", i, "So you have been graded F2")
    else:
        print("Your mark is", i, "So you have been graded F3")
