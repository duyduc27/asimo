# Exercise 16.6 from 1 to 5
import copy
from unit_tester import test
class Point:
    """ Create a new point at coordinates x, y"""
    def __init__(self, x= 0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """ A class to manufacture ractangle objects """
    def __init__(self, pons, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.conner = pons
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.conner, self.width, self.height)

    def area(self):
        """ Return area of any rectangle instance """
        area = self.width * self.height
        return area

    def perimeter(self):
        """ return perimeter of any rectangle instance """
        perimeter = (self.width + self.height)*2
        return perimeter

    def flip(self):
        """ swap width and height of any rectangle instance """
        a = copy.copy(self.height)
        b = copy.copy(self.width)
        self.width = a
        self.height = b

    def contains(self, target):
        """ Test if a point falls within the rectangle"""
        upper_x = self.conner.x  + self.width # Convert upper bound (x direction) to coordinate value
        upper_y = self.conner.y + self.height # Conert upper bound (y direction) to coordiante value
        if  self.conner.x <= target.x < upper_x and self.conner.y <= target.y < upper_y:
            return True
        else:
            return False

    def contains2(self, target): # Version for checking rectangles clashed
        """ Test if a SIDE of the rectangle clashed with sides in another rectangle"""
        side_x = self.conner.x  + self.width
        side_y = self.conner.y + self.height
        if  self.conner.x <= target.x <= side_x and self.conner.y <= target.y <= side_y:
            return True
        else:
            return False

r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
test(r.perimeter() == 30)

n = Rectangle(Point(100, 50), 10, 5)
test(n.width == 10 and n.height == 5)
n.flip()
test(n.width == 5 and n.height == 10)

r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))
test(r.contains(Point(0, 0)))


def rectangles_classed(main, target):
    """ Determine if two rectangles clashsed """
    upperx_target = target.conner.x + target.width
    uppery_target = target.conner.y + target.height
    # We will check 3 points of target rectangle (conner, upperx_target, uppery_target)
    # If one of them was contained in main rectangle
    if main.contains2(target.conner) or main.contains2(Point(upperx_target, target.conner.y)) \
    or main.contains2(Point(target.conner.x, uppery_target)):
        return True
    else:
        return False

r = Rectangle(Point(2, 2), 3, 2)
test(rectangles_classed(r, Rectangle( Point(1, 2), 2, 1)))
test(rectangles_classed(r, Rectangle(Point(4, 1), 2, 3)))
test(not rectangles_classed(r, Rectangle(Point(0, 0), 1, 1)))
test(not rectangles_classed(r, Rectangle(Point(6, 4), 1, 1)))
test(rectangles_classed(r, Rectangle(Point(6, 4), -2, 1)))