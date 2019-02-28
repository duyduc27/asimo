from unit_tester import test

def count(target, nested_lis):
    """ Return number of occurrences of target in a nested list """
    ct = 0 # Initial count
    for i in nested_lis:
        if type(i) == type([]):
            ct += count(target, i)
        else:
            if i == target:
                ct +=1 # basic case
    return ct

test(count(2, []) == 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a",
     [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)