# Exercise 6.9.2 3 4 5 6 7 8 9 10 OK
import sys
def hours_in(i):
    '''Return integer number of hour from total number of seconds'''
    return (i//3600)
def minutes_in(i):
    '''Return integer number of minute from total number of seconds,
    once the hours have been taken out.'''
    return (i % 3600 //60)
def seconds_in(i):
    '''Return the left over seconds'''
    return int((i % 3600) %60)


def to_secs(h,m,s):
    """Convert time to seconds"""
    s1 = h*3600 + m*60 + s
    return int(s1)


def days_in_month(i):
    '''Convert name of month into number days of the month'''
    if i == "January":
        return 31
    elif i == "February":
        return 28
    elif i == "March":
        return 31
    elif i == "April":
        return 30
    elif i == "May":
        return 31
    elif i == "June":
        return 30
    elif i == "July":
        return 31
    elif i == "August":
        return 31
    elif i == "September":
        return 30
    elif i == "October":
        return 31
    elif i == "November":
        return 30
    elif i == "December":
        return 31
    else:
        return None


def day_add(a, b):
    ''' Give a name of today (a) and length of vacation days (b).
    Compute to give result the name of day return '''
    day_num(a)
    c = (day_num(a) + b) % 7
    return day_name(c)



def day_name(i):
    ''' Convert an integer number 0 to 6 into the name of a day'''
    if i == 0:
        return "Sunday"
    elif i == 1:
        return "Monday"
    elif i == 2:
        return "Tuesday"
    elif i == 3:
        return "Wednesday"
    elif i == 4:
        return "Thursday"
    elif i == 5:
        return "Friday"
    elif i == 6:
        return "Saturday"
    else:
        return None


def day_num(i):
    ''' Convert name of a day into an integer number'''
    if i == "Sunday":
        return 0
    elif i == "Monday":
        return 1
    elif i == "Tuesday":
        return 2
    elif i == "Wednesday":
        return 3
    elif i == "Thursday":
        return 4
    elif i == "Friday":
        return 5
    elif i == "Saturday":
        return 6
    else:
        return None

def test(didpass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if didpass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(3 % 4 == 0) # false
    test(3 % 4 == 3) # true
    test(3 / 4 == 0) # false
    test(3 // 4 == 0) # true
    test(3+4  *  2 == 14) #false
    test(4-2+2 == 0) # failse
    test(len("hello, world!") == 13) # true

test_suite()