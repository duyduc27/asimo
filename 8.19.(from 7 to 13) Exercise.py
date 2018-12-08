# Exercise 8.19.7 8 9 10 11 12 13
import sys
def remove_all_1(ch, seq): # 8.19.3
    """Remove all specify substring occurence from a string"""
    a = seq
    while a:
        # Use a while loop and repeatly calling remove function (from 8.19.12 Exercise) till have nothing to remove
        if remove(ch, a) == a:
            return remove(ch, a)
        else:
            a = remove(ch, a)
            

def remove_all(ch, seq): # 8.19.3
    """Remove all specify substring occurence from a string"""
    # Cheating, I peeked over about string method in manual
    # I haven't had solution without using replace method at this time
    return seq.replace(ch, "") # Remove substring by replacing a empty sequence



def remove(ch, seq): # 8.19.12
    """ Remove the first specify substring occurence from a string """

    """ Thinking: we need length of this substring for slicing.
    And then add 2 rest parts"""
    pos = seq.find(ch)
    if pos != -1:
        new_seq = seq[0: pos] + seq[(pos +len(ch)):]
        return new_seq
    else:
        return seq # Have nothing to remove


def count(ch, seq): # 8.19.11
    """ Counting how many times a substring occurs in a string"""
    # Hey Asimo here, get back to 8.19.4. I ready did that solution
    count = 0 # Set initial count value
    pos = 0 # Set initial position value
    while pos < len(seq):
        if seq.find(ch, pos) != -1: # Open Python manual and read about find method
            count += 1
            pos = seq.find(ch, pos) +1
        else:
            break
    return count



def is_palindrome(seq): # 8.19.10
    """ Check if this seq is palindrome or not """
    if seq == reverse(seq):
        return True


def remove_letter(ch, seq): #8.19.9
    """ Remove all leter occur in a sequence """
    rm_seq = ""
    for i in range(0, len(seq)):
        if seq[i] != ch:
            rm_seq += seq[i]
    return rm_seq


def mirror(seq): # 8.19.8
    """ Make a mirror of sequence """
    mr_seq = seq + reverse(seq)
    return mr_seq


def reverse(seq): # 8.19.7
    """ Reverse sequence """
    new_seq = ""
    for i in range(1, len(seq) +1): # Because I want to use index -1 for reversing
        new_seq += seq[-i] # So I did the range for that purpose
    return new_seq


def test(did_pass):
    """Printing the result of a test"""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is FAILED".format(linenum)
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module """
    test(reverse("happy") == "yppah") # 8.19.7
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(mirror("good") == "gooddoog") # 8.19.8
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    test(remove_letter("a", "apple") == "pple") # 8.19.9
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "") # Recorrected systax error
    test(remove_letter("b", "c") == "c") # Recorrected systax error
    test(is_palindrome("abba")) # 8.19.10
    test(not is_palindrome("abab") ==True)
    test(is_palindrome("tenet") ==True)
    test(not is_palindrome("banana") ==True)
    test(is_palindrome("straw warts") ==True)
    test(is_palindrome("a") ==True)
    test(is_palindrome("") == True)
    test(count("is", "Mississippi") == 2) #8.19.11
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    test(remove("an", "banana") == "bana") # 8.19.12
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")
    test(remove_all("an", "banana") == "ba") # 8.19.13
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite() # Here is the call to run the tests



