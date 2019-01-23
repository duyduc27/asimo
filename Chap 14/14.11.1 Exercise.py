# Exercise 14.11.1
from unit_tester import test

def find_item_share_in_blist(lis1, lis2):
    """ Return only those items that are present in both sorted lists"""
    result = [] # Create initial result
    for i in lis1:
        if i in lis2:
            result.append(i)
    return result


test(find_item_share_in_blist([1,2,3,4], [1,4,7,8]) == [1,4])
test(find_item_share_in_blist(["a", "b", "c", "d"], ["a", "c", "e"]) == ["a", "c"])


def find_unique_item_in_first(lis1, lis2):
    """ Return only those items that are present in 1st list, but not 2nd list"""
    result = [] # Create initial result
    for i in lis1:
        if i not in lis2:
            result.append(i)
    return result

test(find_unique_item_in_first([1,2,3,4], [1,4,7,8]) == [2,3])
test(find_unique_item_in_first(["a", "b", "c", "d"], ["a", "c", "e"]) == ["b","d"])


def find_unique_item_in_second(lis1, lis2):
    """Return only those items that are present in the second list,
    but not in the first."""
    result = [] # Create initial result
    for i in lis2:
        if i not in lis1:
            result.append(i)
    return result

test(find_unique_item_in_second([1,2,3,4], [1,4,7,8]) == [7,8])
test(find_unique_item_in_second(["a", "b", "c", "d"], ["a", "c", "e"]) == ["e"])

def find_present_item_in_either_blist(lis1, lis2):
    """Return items that are present in either the first or the second list."""
    xi = 0
    yi = 0
    result = [] # Set initial result and initial indices in both lists
    while True:
        if xi >= len(lis1): # If lis1 is finished
            result.extend(lis2[yi:]) # Add remaining of lis2
            return result

        if yi >= len(lis2): # If lis2 is finished
            result.extend(lis1[xi:]) # Add remaining of lis1
            return result

        if lis1[xi] <= lis2[yi]: # Value lis1 at index xi come first
            result.append(lis1[xi])
            xi += 1

        else:
            result.append(lis2[yi])
            yi += 1

    return result


test(find_present_item_in_either_blist([1,2,3,4], [1,4,7,8]) == [1,1,2,3,4,4,7,8])
test(find_present_item_in_either_blist
(["a", "b", "c", "d"], ["a", "c", "e"]) == ["a", "a", "b", "c", "c", "d", "e"])

def bagdiff(lis1, lis2):
    """ Return items from the 1st list that are not eliminated by matching
    element in 2nd list. An item in the second list “knocks out” just one
    matching item in the first list in this case"""
    xi = 0
    yi = 0
    result = [] # Set initial result and initial indices in both lists
    while True:
        if xi >= len(lis1): # If lis1 is finished
            return result

        if yi >= len(lis2): # If lis2 is finished
            result.extend(lis1[xi:]) # Add remaining of lis1
            return result

        if lis1[xi] < lis2[yi]:
            result.append(lis1[xi])
            xi +=1

        elif lis1[xi] > lis2[yi]: # Come to next values in lis2 to compare
            yi +=1

        else:
            xi +=1 # Eliminate one item matching in lis2
            yi +=1


test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
test(bagdiff(["a","b", "c", "c", "d"], ["a", "c", "e"]) == ["b", "c", "d"])
