# Exercise 14.11.2
from unit_tester import test

def share_diagonal(x0,y0,x1,y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0) # Calculate absolute y distance
    dx = abs(x1 - x0) # Calculate absolute x distance
    return dy == dx # They clash if dy = dx

test(not share_diagonal(0,0,2,1))
test(share_diagonal(0,0,3,3))
test(share_diagonal(1,2,3,0))

def col_clashes(bd, col):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(col):
        if share_diagonal(i, bd[i], col, bd[col]):
            return True
    return False

test(not col_clashes([0,3,4,2,1], 3))
test(not col_clashes([0,3,4,2,1], 1))
test(col_clashes([0,3,4,2,1], 2))
test(col_clashes([0,3,4,2,1], 4))

def has_clashes(bd):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for i in range(1, len(bd)):
        if col_clashes(bd, i):
            return True
    return False

test(has_clashes([0,3,4,2,1]))
test(has_clashes([0,3,5,2,4]))
test(not has_clashes([1,3,5,2,4]))
test(not has_clashes([1,3,5,]))

def main(n):
    import random
    rng = random.Random() # Invoke a generator

    basic_permutation = list(range(n))
    tries = 0 # Set initial probe
    sol = 0 # Set initial solution
    while sol < 10:
        tries += 1
        rng.shuffle(basic_permutation)
        if not has_clashes(basic_permutation):
            #print("Solution is {0} in {1} tries.".format(basic_permutation, tries))
            sol += 1
            tries = 0 # Found solution, reset tries for next solution
import time
t0 = time.clock()
main(4)
t1 = time.clock()
print("With board size is 4 and maximum 10 solutions. It took {0:.4f} seconds".format(t1-t0))

t2 = time.clock()
main(12)
t3 = time.clock()
print("With board size is 12 and maximum 10 solutions. It took {0:.4f} seconds".format(t3-t2))

t4 = time.clock()
main(16)
t5 = time.clock()
print("With board size is 16 and maximum 10 solutions. It took {0:.4f} seconds".format(t5-t4))

# The maximum size puzzle is 13 that usually solve under 1 min. ~ 41.7849 seconds


