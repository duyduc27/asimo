#Exercise 8.19.1 2 3 4
import sys
# 8.19.1 in test suite
def count_letters1(seq, ch, pos = 0): # 8.19.4
    """
    Add third parameter and repeatedly calls the find method
    Position is where we want to start. With 0 is default value
    """
    count = 0
    while pos < len(seq):
        if seq.find(ch, pos) != -1: # Still can find our character
            """ Note: built-in find(sub,start,end)
            Read more in Python manuals """
            count +=1
            pos = seq.find(ch, pos) +1
        else:
            break # Exit loop if can't find any more our character
    return count




def count_letters(seq, ch): # 8.19.3
    """ Accept strings and characters as arguments
    Function returns number of character"""
    count = 0
    for i in seq:
        if i == ch:
            count += 1
    return count



def modify_name_duckling(): # 8.19.2
    """ Modify previous program for correcting name of ducklings"""
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O":
            letter = "Ou"
        elif letter == "Q":
            letter = "Qu"
        print(letter + suffix)

def test(did_pass):
    """ Print result if the test pass or not """
    linenum = sys._getframe(1).f_lineno # Get order number of line
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print (msg)


def test_suite():
    """ Use a collection of test for checking this module """
    test("Python"[1] == "y") # 8.19.1
    test("Strings are sequences of characters."[5] == "g")
    test(len("wonderful") == 9)
    test("Mystery"[:4] == "Myst")
    test(("p" in "Pineapple") == True)
    test(("apple" in "Pineapple") == True)
    test(("pear" not in "Pineapple") == True)
    test(("apple" > "pineapple") == False)
    test(("pineapple" < "Peach") == False) #8.19.1
    test(count_letters("Iam not smart", "a") == 2 ) # 8.19.3
    test(count_letters1("Banana", "a") == 3 ) # 8.19.4
    test(count_letters1("Banana", "y") == 0 ) # 8.19.4

test_suite() # Call the test suite