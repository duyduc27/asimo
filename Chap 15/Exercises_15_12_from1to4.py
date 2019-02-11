# Exercise 15.12 from 1 to 4
from math import sqrt
from unit_tester import test
class Point:
    """ Create a new point, at coordinate x, y"""
    def __init__(self, x=0 , y =0):
        """ Create a new point at x, y"""
        self.x = x
        self.y = y

    def reflect_x(self):
        """ Return new point that is the reflection of the point
        about the x-axis"""
        return Point(self.x, - self.y)

    def slope_from_origin(self):
        """ Compute slope (độ dốc/ hệ số góc) from orgin point """
        return (self.y)/(self.x)

    def get_line_to(self, p2):
        """ return the two coefficients of equation of
        a straight line is “y = ax + b” """
        a = (p2.y - self.y)/ (p2.x -self.x) # slope between 2 points
        b = self.y - a*self.x
        return Point(a,b)


def distance(p1, p2):
    """ Compute distance between 2 points """
    return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

p = Point(1,2)
q = Point(4,6)
test(distance(p, q) == 5)

k = Point(3, 5).reflect_x()
test((k.x, k.y) == (3, -5))

test(Point(4, 10).slope_from_origin() == 2.5)
# This method failed when target point have x coordinate equal 0

l = Point(4, 11).get_line_to(Point(6, 15))
test((l.x, l.y) == (2, 3))
# This method failed when x coordinate of each point equal 0