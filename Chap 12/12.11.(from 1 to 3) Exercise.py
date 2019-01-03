# Exercise 12.11.1 2 3
import calendar
cal = calendar.TextCalendar(3)  # Create an calendar, that start from thursday
cal.pryear(2012)                # What happens here?
# Print the calender for an entire year

print("------------------------------------------------") # Make a newline to seprate my stuffs

def my_bir_month(m):
    """ Print the month which your birthday occurs"""
    cal = calendar.TextCalendar(3)
    cal.prmonth(2012, m)

my_bir_month(4)

print("------------------------------------------------") # Make a newline to seprate my stuffs

d = calendar.LocaleTextCalendar(6, "VIETNAMESE")
d.pryear(2012)

# Font showed up wrong


calendar.isleap(2012)

# Argument is year, return True if this is currently year what we set
# A Boolean function type: "type(calendar.isleap(2012))"

""" So with Calender module, we also have to import this module for using it.
With object Calender and method TextCalendar(firstweekday=0)
Set LocaleTextCalendar(6, "VIETNAMESE") attributes method for our object
It will return wrong font because it's always return as unicode (not all of
localization using unicode)
We also can check the year of calender is what we want by using
calendar.isleap(year)
"""

# Exercise 12.11.2

"""
a) There are 45 functions (I didn't count constants - 5)
b) math.ceil(x) return a smallest integer number greater than or equal to x
   math.floor(x) return a largest integer number less than or equal to x
c) We compute square root through the express: x**(1/2)
d) Data constants in math module aren't methods of a object, kindda "pure"

Note: I think there are too much functions in math module, I don't think
we are going to use even a half.
At first, I think method math.ceil(x) and math.floor(x), we can use it like
round() function but it's not! That is a kind of measure, depend if you want to
get higher integer value or lower integer value of a float number.
"""

# Exercise 12.11.3

"""
In copy module, deepcopy(x) method constructs a new object and then
inserts copies into it of the object found in the original.
That mean we have 2 objects, but have same identifier elements (ID).

We can use this method for 11.22.11 Exercise in List chapter
"""

print("------------------------------------------------") # Make a newline to seprate my stuffs
print("---------------Exercise 12.11.3-----------------") # Make a newline to seprate my stuffs

import copy

def swap(x, y):      # Incorrect version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)
     return x,y

a = ["This", "is", "fun"]
b = [2,3,4]

print("before swap function call: a:", a, "b:", b)
a,b = copy.deepcopy(swap(a,b))

print("after swap function call: a:", a, "b:", b)

