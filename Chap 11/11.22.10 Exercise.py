# Exercise 11.22.10
import sys

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

def replace(s, old, new):
    """ Replace all occurrence of old with new in s string """
    return new.join(s.split(old))


def test(did_pass):
    """ Print result of a test """
    linenum = sys._getframe(1).f_lineno # Get caller's line number
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)

def test_suite():
    """Run the suite of tests for code in this module """
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite() # Here is the call to run the tests