# Exercise 12.11.7
import unit_tester # Module unit_tester scaffolding from chap 6

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    if old.isspace(): # If a weird guy set "old" only have space(s)
        old = None
    return new.join(s.split(old))

unit_tester.test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
unit_tester.test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")