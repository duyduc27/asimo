# Exercise 7.26.9
def print_triangular_numbers(n):
    '''Create a board with right column is triangular number'''
    for i in range(1, n +1):
        t = int((i + 1)*i /2)
        print(i, "      ", t)
    print()

print_triangular_numbers(5)