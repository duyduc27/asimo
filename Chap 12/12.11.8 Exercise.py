# Exercise 12.11.8
import string
from unit_tester import test # Module unit_tester scaffolding from chap 6

def cleanword(s):
    """ Remove punctuation for clean words """
    clean_s = ""
    for i in s:
        if i not in string.punctuation:
            clean_s += i
    return clean_s

def has_dashdash(s):
    """ Check if string have double dash or not """
    if s.find("--") == -1 : # Don't have double dash
        return False
    else:
        return True

def extract_words(s):
    """ Split words without spaces and punctuation
    In this case, I don't think reuse has_dashdash(s) function is a good idea
    Because not only case "dashdash", maybe have other cases e.g.
    "question-question", "dot-dot", etc. and we want to get real "pure"
    words right?
    """
    clean_s = ""
    for i in s:
        if i not in string.punctuation:
            clean_s += i
        else:
            i = " " # Changed punctuation to space and we can clear after that
            clean_s += i

    n = clean_s.lower() # Convert all char to lowercase
    return n.split()

def wordcount(wd, seq):
    """Count specify word in a sequence"""
    ct = 0 # Set initial count
    for i in seq:
        if i == wd:
            ct += 1
    return ct

def wordset(seq):
    """ Find word set in a sequence """
    w_set = []
    for i in sorted(seq):
        if i not in w_set:
            w_set.append(i)
    return w_set

def longestword(seq):
    """ Find the word has the longest length """
    l_length = 0
    for i in seq:
        if len(i) >= l_length:
            l_length = len(i)
    return l_length

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")
test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))
test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])
test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)
test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])
test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)