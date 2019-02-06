# Exercise 14.11.5
from unit_tester import test

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

def lotto_draw():
    """ Simulate a lotto draw """
    import random
    rng = random.Random()

    result = [] # Set initial result
    ball = 0 # Set initial ball
    while ball < 6: # draw 6 balls
        value = rng.randrange(1,50) # random balls numbered from 1 to 49
        if value not in result: # Pick balls from bag without replacement
            result.append(value)
            ball += 1

    return result


def lotto_match(draw, ticket):
    """ Compare a single ticket and a draw
    return the number of correctly picks on that ticket"""
    cor_pick = 0 # Set initial corretly pick
    for i in ticket:
        if i in draw:
            cor_pick +=1
    return cor_pick

test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)

def lotto_matches(draw , tickets):
    """ Return a list that telling the number of correctly picks on each ticket"""
    result = [] # Set initial result
    for i in tickets:
        number = lotto_match(draw, i) # Number of correctly picks on this ticket
        result.append(number)
    return result

test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

def is_prime_num(n):
    """Check if the number is prime number """
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True


test(is_prime_num(3))
test(is_prime_num(5))
test(not is_prime_num(4))
test(not is_prime_num(9))

def primes_in(lis):
    """ Check list of integers, return the number of primes in this list"""
    count = 0 # Set initial count
    for i in lis:
        if is_prime_num(i):
            count +=1
    return count

test(primes_in([42, 4, 7, 11, 1, 13]) == 3)

def merge_lis(lis):
    """ Merge those lists to a new list without duplicates"""
    result = [] # Set initial result
    new_lis = [] # Set initial list
    for i in lis: # Sort sub lists in a list
        new_lis.extend(i)
    new_lis.sort() # Make elements in order
    for i in new_lis:
        if i not in result: # Omit if the element was ready in
            result.append(i)
    return result


test(merge_lis([[12, 11,2,4], [2,4,12], [1,2,3]]) == [1,2,3,4,11,12])

def produce_prime_num_lis(start, stop):
    """ Produce a prime number list """
    result = []
    for i in range(start,stop):
        if is_prime_num(i):
            result.append(i)
    return result

test(produce_prime_num_lis(2,12) == [2, 3, 5, 7, 11])

def prime_misses(lis):
    """ Check each sub list, if mother list missed any prime numbers
    Then return a list of all prime numbers that they were missed"""
    # In this case. In mother list, each sub list is ready a prime numbers sequence
    result = []
    n_lis = merge_lis(lis) # Merge mother list
    p_lis = produce_prime_num_lis(2, 50) # Create prime list
                                        # Because we have 49 balls and prime number start from 2
    ni = 0
    pi = 0
    while True:
        # Note: in this case p_lis >= n_lis (for sure)
        # So we eliminate some conditions
        if ni >= len(n_lis): # There are no more elements in n_lis
            result.extend(p_lis[pi:])
            return result

        # Both lists still have items, copy smallest item to result
        if p_lis[pi] < n_lis[ni]: # But this case will never happen
            result.append(p_lis[pi]) # add missed prime number to result
            pi +=1

        elif n_lis[ni] == p_lis[pi]:
            ni +=1
            pi +=1


test(prime_misses(my_tickets) == [3, 29, 47])


def compare_ticket(tickets, n, m):
    """ Average out the number of draws needed until one of the
    computer scientist’s tickets has at least 3 correct picks.
    Average out in n times"""
    total = []
    total_draw_needed = 0
    k = 0
    n = 0
    while n<20:
        draw = lotto_draw() # Create a draw
        k += 1
        for ticket in tickets:
            if lotto_match(draw, ticket) >= m:
                print("Our draw is: ",draw)
                print("We need {0} times draw for our tickets have at least {1} correct picks".format(k,m))
                total.append(k)
                k = 0
                n += 1
    for i in total:
        total_draw_needed += i
    average = total_draw_needed / n
    print("The average of {0} times tried for having at least {1} correct picks are {2:.2f} draws".format(n, m,average))


#* compare_ticket(my_tickets, 20, 3) # Tickets of the scientist, experiment in 20 times, at least 3 correct picks
#* compare_ticket(my_tickets, 20, 4)
compare_ticket(my_tickets, 20, 5)
