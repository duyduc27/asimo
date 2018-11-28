# Exercise 7.26.1 2 3 4 5 6
import sys
num_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num_list1 = (1, 3, 5, 7)
word_list = ("Asimo", "Duy Duc", "I'm really serious", "that's", "right")
word_list1 = ("sam", "sadam", "sadness" , "sand", "saber")
word_list2 = ("sadam", "sadness" , "sand", "saber", "sam")

def ct_word_have_sam(mylist):
    """Count how many words occur in a list up to and
    including the first occurrence of the word “sam”."""
    count = 0

    """Check if "sam" is the first occurrence of word in this list"""
    for i in mylist:
        if mylist[0] == "sam":
            count += 1
        else:
            return None
    return count


def sum_except_first_one(mylist):
    """Sum all the elements list except the first even number."""
    sum1 = 0
    sum2 = 0

    """Find the first even number"""
    for i in mylist:
        if i % 2 == 0:
            sum2 += i
            break

    """Sum up all elements and do subtraction from the first even number"""
    for i in mylist:
        sum1 += i
    return sum1 - sum2


def ct_word():
    """Count words in list have length 5"""
    count = 0
    for i in word_list:
        if len(i) == 5:
            count += 1
    return count


def ct_odd_num():
    """Count how many odd numbers are in a list"""
    count = 0
    for i in num_list:
        if i % 2 != 0:
            count += 1
    return count


def sum_even_num():
    """Sum up all the even numbers in a list"""
    sum_even = 0
    for i in num_list:
        if i %2 == 0:
            sum_even += i
    return sum_even


def sum_negative_num():
    """sum up all the negative numbers in a list"""
    sum_neg = 0
    for i in num_list:
        if i < 0:
            sum_neg += i
    return sum_neg


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)


def test_suite():
    # A collection tests for code in this module
    test(ct_odd_num() == 5)
    test(sum_even_num() == 20)
    test(sum_negative_num() == 0)
    test(ct_word() == 2)
    test(sum_except_first_one(num_list)== 43) # test on num_list
    test(sum_except_first_one(num_list1)== 16) # test on num_list1 without even numbers
    test(ct_word_have_sam(word_list1) == 5) # test on word_list1 with the first word is "sam"
    test(ct_word_have_sam(word_list2) == None)


test_suite() #Call a collection of tests

