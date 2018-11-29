# Exercise 7.26.10
import sys
def is_prime(n):
    """Checkout if the integer is prime or not"""
    if n < 2:
        return None
    else:
        for i in range(2, n):
            if n % i == 0:
                return None
            else:
                return True


def test(did_pass):
    """Print the result of a test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)


def test_suite():
    """Run a collection of tests for checking code in this module"""
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(4491))

test_suite() # Here is the call to run the tests

