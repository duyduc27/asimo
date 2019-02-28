from unit_tester import test
def flatten(nested_lis):
    """" Return simple list containing all values in a nested list """
    sim_lis = [] # Initial result
    for i in nested_lis:
        if type(i) == type([]):
            sim_lis.extend(flatten(i))
        else:
            sim_lis.append(i)
    return sim_lis

test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])