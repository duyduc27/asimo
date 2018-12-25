# Exercise 11.22.1 2 3 4

"""
11.22.1
list(range(10, 0, -2))
Python interpreter will make a list from 10 to 0 with step -2
If start < stop and step is negative integer that will return an empty list.
Relationship among start, stop, step ???
    start < stop and step > 0 -> return a list
    start < stop and step < 0 -> return empty list
    start > stop and step < 0 -> return a list
    step = 0 -> error occur
"""

"""
11.22.2

This fragment code will create only one turtle. Because turtle mode is not
immutable type. So Python interpreter won't use as 2 objects.
Now "tess" and "alex" are 2 alias of 1 turtle so you change color of 1
that mean you did with the turtle.
"""

""""
11.22.3

https://ibb.co/mTz0rJT
"""

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

# There are 2 list with same values in first result
# There are 2 alias of a list