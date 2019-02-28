
def fib(n):
    """ Rewrite fibonacci without using recursion """
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            a, b = b, a+b
            # Note: because there are immutable data values
            # So we have to do this one to assign values!
        return b
# We can do fib(200) with fast result without problems than recursion way!
