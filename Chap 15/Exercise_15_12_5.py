# Exercise 15.12.5
class Point:
    """ Create a new point at coordinates x, y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

a = Point(1,2)
b = Point(5,2)
c = Point(1,-3)

def mid_point(a, b, c):
    """ Find mid point when have 3 points lying on the circle
    The formula:
    https://math.stackexchange.com/questions/1893599/center-of-circle-given-4-points
    """
    d = 2*(a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y))

    rx = ((a.x**2 + a.y**2)*(b.y - c.y) + (b.x**2 + b.y**2)*(c.y - a.y) +
    (c.x**2 + c.y**2)*(a.y -b.y))/d

    ry = ((a.x**2 + a.y**2)*(c.x - b.x) + (b.x**2 + b.y**2)*(a.x - c.x) +
    (c.x**2 + c.y**2)*(b.x -a.x))/d

    return Point(rx, ry)


n = mid_point(a, b, c)
# Note: only need 3 points that fall on the circumference of a circle
# to find the mid point of the circle
# I don't know how this formula work so please spare for me!

# This function will fall when the condition: d = 0