# Exercise 11.22.5 6 7 8
import sys
def cross_product(u, v): #11.22.8
    # https://www.mathsisfun.com/algebra/vectors-cross-product.html
    new_list = [u[1]*v[2]-u[2]*v[1],
                u[2]*v[0]-u[0]*v[2],
                u[0]*v[1]-u[1]*v[0]]
    return new_list



def dot_product(u, v): #11.22.7
    n = 0 # Make an initial value of dot product
    new_list = [] # Make an initial list
    for i in range(len(u)):
        m = u[i] * v[i]
        new_list.append(m)
    for i in new_list:
        n += i
    return n


def scalar_mult(s, v):  #11.22.6
    """take a number, s, and a list, v and returns the scalar multiple
    of v by s."""
    new_list = []
    for i in range(len(v)):
        m = v[i] * s
        new_list.append(m)
    return new_list


def add_vectors(u, v): #11.22.5
    """ u and v are 2 lists of numbers have same length
    Make an initial result by empty list"""
    new_vector = []
    """Because they have same length so we
    should take advantage from this one"""
    for i in range(len(u)):
        m = u[i] + v[i] # Get their value of i index at the same time!
        new_vector.append(m)
    return new_vector

def test(did_pass):
    """ Print the result of a test"""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module """
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    test(cross_product([2,3,4], [5,6,7]) == [-3, 6, -3])

test_suite() # Here is the call to run the tests


