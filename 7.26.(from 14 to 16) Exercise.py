# Exercise 7.26.14 15 16
import sys
def sum_of_squares(xs):
    """compute the sum of the squares of the numbers in the list"""
    sum_sq = 0
    for i in xs:
        sum_sq += i**2
    return sum_sq



def num_even_digits(n):
    """ Count number of even digits """
    count = 0
    if n == 0:
        count = count + 1
    elif n < 0:
        n = abs(n)

    while n != 0:
        if n % 2 == 0: # Check if the last digit is even number
            count += 1
        n = n // 10 # Decrease a digit
    return count


def num_digits(n):
    """ Calculate digits of a number """
    count = 0
    if n == 0:
        count = count + 1
    elif n < 0:
        n = abs(n)

    while n != 0:
        count = count + 1
        n = n // 10
    return count


def test(did_pass):
    """print out test result"""
    linenum = sys._getframe(1).f_lineno # Get index of line
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)

def test_suite():
    """ Run a test suite for checking code of this module """
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)

test_suite() # Call this collection test