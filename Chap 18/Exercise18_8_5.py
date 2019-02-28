from unit_tester import test
def recursive_min(nested_nlis):
    """ Return smallest number of nested number list """
    s_num = None
    first_try = True # flag
    for i in nested_nlis:
        if type(i) == type([]):
            val = recursive_min(i)
        else:
            val = i

        if first_try or val < s_num:
            s_num = val # basic case
            first_try = False
    return s_num



test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)