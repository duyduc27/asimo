# Exercise 14.11.3
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
    tries = 0 # Set initial probe
    sol = 0 # Set initial solution
    result = [] # Set initial result
    while sol < 10:
        tries += 1
        permutation = generate_random_permutation(n)
        if not has_clashes(permutation) and permutation not in result:
            result.append(permutation)
            print("Solution is {0} in {1} tries.".format(permutation, tries))
            sol += 1
            tries = 0 # Found solution, reset tries for next solution


def generate_random_permutation(k):
    """ generate a random permutation list in K things """
    """ Note: We really need this one. Because shuffle method only shuffle
    sequence x "in place". That mean, we didn't create new object and
    just only replace inside the ready one. We have to store it by another way.
    """
    import random
    rng = random.Random() # Invoke a generator
    basic_permutation = list(range(k))
    rng.shuffle(basic_permutation)
    return basic_permutation

main(8) # Board 8x8
# Notice about available solutions too. In board 8x8 has 92 unique solutions > 10
# But not in board 4x4 (only 2 unique solutions < 10) !