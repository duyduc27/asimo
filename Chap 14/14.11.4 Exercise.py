# Exercise 14.11.4
from unit_tester import test

from N_queens import main

def mirror_sol_y_axis(bd):
    """ Mirror a solution in the Y axis """
    # Symmetric in Y axis then y1 = y0 and x1 = -x0
    result = [] # Set initial result
    for i in reversed(bd): # Because elements in ordered and x1 = - x0 so we reverse this list
        result.append(i)
    return result

test(mirror_sol_y_axis([3,1,2,0]) == [0,2,1,3]) # board 4x4, share diagonal
test(mirror_sol_y_axis([None,2,None,1]) == [1,None,2,None]) # board 4x4, no share diagonal

def mirror_sol_x_axis(bd):
    """ Mirror a solution in the X axis """
    # Symmetric in X axis then x1 = x0 and y1 = -y0
    result = [] # Set initial result
    total_elements = len(bd) -1 # Count from 0
    for i in range(len(bd)):
        if bd[i] == None: # If the square containing nothing, "this one is not necessary"
            result.append(None)
        else:
            new_e = total_elements - bd[i] # Because y1 = - y0 with same index, so we calculate y1 by y0
            result.append(new_e)
    return result

test(mirror_sol_x_axis([None,2,None,1]) == [None,1,None,2])
test(mirror_sol_x_axis([3,1,2,0]) == [0,2,1,3])

def relocate_sol_90d(bd):
    """ relocate a solution by 90 degrees """
    """ Explain: when we relocate a solution by 90 degrees then the Y0 axis of
    original solution was turned into X1 axis of permutation. Thus, we ready have
    'indices' of the permutation by 'values' of bd - board.
    And Y1 equals X1 go forward to N square (board NxN)
    """
    result = list(range(len(bd))) # Create a list that has same element of BD
    for i in bd: # traverse BD for edting values purpose
        result[i] = len(bd) -1 - bd.index(i)
        # Edit values from 'result', we have to subtract 1,
        # because Y1 was counted from 0
    return result

def relocate_sol_180d(bd):
    """ relocate a solution by 180 degrees """
    a = bd
    for i in range(2): # multiply 90 degrees by 2 then get 180 degrees
        a = relocate_sol_90d(a)
    return a

def relocate_sol_270d(bd):
    """ relocate a solution by 180 degrees """
    a = bd
    for i in range(3): # multiply 90 degrees by 3 then get 270 degrees
        a= relocate_sol_90d(a)
    return a

test(relocate_sol_90d([0,4,7,5,2,6,1,3]) == [7,1,3,0,6,4,2,5])
test(relocate_sol_180d([0,4,7,5,2,6,1,3]) == [4,6,1,5,2,0,3,7])
test(relocate_sol_270d([0,4,7,5,2,6,1,3]) == [2,5,3,1,7,4,6,0])

def symmetry_in_a_linear1(bd):
    """ symmetry in a linear y=x """
    # So X1 = Y0 and Y1 = X0
    result = list(range(len(bd)))
    new_bd = result
    for i in bd:
        new_bd[i] = bd.index(i)
    return new_bd

test(symmetry_in_a_linear1([0,4,7,5,2,6,1,3]) == [0,6,4,7,1,3,5,2])

def symmetry_in_a_linear2(bd):
    """ symmetry in a linear y=-x """
    # So X1 = -Y0 and Y1 = - X0
    result = list(range(len(bd))) # Create a list with same elements
    x1 = []
    for i in bd:
        x1.append(len(bd) -1 -i)
    y1 = list(reversed(list(range(len(bd))))) # Create list of bd indices
    for e in x1:
        result[e] = y1[x1.index(e)]
    return result


test(symmetry_in_a_linear2([0,4,7,5,2,6,1,3]) == [5,2,4,6,0,3,1,7])

def generate_family_symmetries(bd):
    """ generate family of symmetries for a solution """
    result = [] # Set initial result
    result.append(bd)
    result.append(relocate_sol_90d(bd))
    result.append(relocate_sol_180d(bd))
    result.append(relocate_sol_270d(bd))
    result.append(mirror_sol_y_axis(bd))
    result.append(symmetry_in_a_linear1(bd))
    result.append(mirror_sol_x_axis(bd))
    result.append(symmetry_in_a_linear2(bd))

    return result

test(generate_family_symmetries([0,4,7,5,2,6,1,3]) ==
[[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
 [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
 [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
 [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]])

# N_queens.py for 14.11.4 e