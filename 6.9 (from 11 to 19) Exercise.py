# Exercise 6.9.11 12 13 14 15 16 17 18 19 OK
import sys
def c2f(t):
    '''Convert Celsius degrees to Fahrenheit degrees'''
    return round(t*1.8 +32)

def f2c(t):
    '''Convert Fahrenheit degrees to Celsius degrees'''
    return round((t-32)/ 1.8)



def is_multiple(a, b):
    '''Check if a is multiple of b'''
    if is_factor(b, a) == True:
        return True
    else:
        return False


def is_factor(f, n):
    ''' Check if f is a factor of n '''
    if n % f == 0:
        return True
    else:
        return False



def is_even(n):
    '''Return true if the integer is even number,
    false if the integer is odd number'''
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    ''' Return true if the integer is odd number,
    flase if the integer is even number'''
    if n % 2 != 0:
        return True
    else:
        return False


def intercept(x1, y1, x2, y2):
    ''' y = mx + b trong đó b là intercept và m là slope '''
    m = slope(x1, y1, x2, y2)
    b = y1 - m*x1
    return b


def slope(x1, y1, x2, y2):
    '''Return the slope of the line through 2 points'''
    return (y2-y1)/(x2-x1)


def hypotenuse(a, b):
    '''Return the length hypotenuse when know two sides
    length of a right triangle'''
    return (a**2 + b**2)**0.5


def compare(a,b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    ''' Run the suite of tests for code in this module (this file)
    '''
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

test_suite() ## Here is the call to run the tests