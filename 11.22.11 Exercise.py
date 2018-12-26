# 11.22.11 Exercise
def swap(x, y):      # Correct version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)
     return x, y

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
a, b = swap(a, b)
print("after swap function call: a:", a, "b:", b)

# a and b still point to their original values after call swap function
""" First at all, this is mutable value - list.
Because arguments are passed by assingment in Python.
Since assignment just creates references to objects. So in this case
our objects (contain list values) didn't modify, we only change reference (x, y)
that refer to the same objects. That didn't effect to code outside (because we
didn't change our object (a, b).
"""

# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference?fbclid=IwAR2WIx4TtybdxojuXlcmn-MWkOfWUrp9Gnbvhgj5FArUh54Nyc4yBUOmLZA
# Solution: https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
# Return our new x, y values at line 6th
# Update values our variable by our swap function: a,b = swap(a,b) at line 11th -> create new objects with our desired value