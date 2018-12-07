# Exercise 8.19.5
import string

quote = """
We got a reputation to protect. Like, if America didn't stand up
everyone would attack it. Well, in our neighbourhood if you don't
stand up you can't walk down the street, 'cause everyone will attack you.
"""

# Quote from "Dangerous minds", hey check it out. This's an awesome movie!

def analyse_seq(seq, ch):
    """ Remove punctuation, break sequence into a list of words
    Count number of words in sequence that contain "e" letter """
    count = 0
    ct_ch = 0
    processing_t = ""
    """First of all, we remove punctuation in our quote
    Then add into new sequence "processing_t" """
    for letter in seq:
        if letter not in string.punctuation:
            processing_t += letter

    """Break sequence into a list of words
    Then count them if each item in loop equal with our character"""
    for i in processing_t.split():
        count += 1 # Count word
        if (ch in i) == True:
            ct_ch += 1 # Count our specific character

    rating = round(ct_ch/count*100,1)  # Precision 1 digits of decimal number

    """Print announcement of our data analysis"""
    print(('Your text contains {0} words, of which {1} ({2}%) contain an "{3}".').format(count, ct_ch, rating, ch))


analyse_seq(quote, "e")