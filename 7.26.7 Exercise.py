# Exercise 7.26.7
def sqrt(a):
    """Modify function square root. Printing out "better" result when
    processing each time in loop"""
    approx = a/2.0
    while True:
        better = (approx + a/approx)/2.0
        print (better)
        if abs(approx - better) < 0.0001:
            return better
        approx = better

sqrt(25)

