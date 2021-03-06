# Exercise 13.11.4
from read2test import read_2_test # import a small module for reading text
def remove_line_num(old, new):
    """ undo numbering from previous exercise """
    infile = open(old, "r")
    xs = infile.readlines() # Turn lines into a list
    infile.close()

    outfile = open(new, "w")
    for i in xs:
        lis_words = i.split(" ") # Extract words from a line
        # We don't use default seq=None at split() method
        # Because that will get rid the "newline" character
        if lis_words[0].isdigit():
            new_seq = lis_words[1:] # Remove numbering
            fully_line = " ".join(new_seq)
            outfile.write(fully_line)
        else:
            outfile.write(i)
    outfile.close()
    read_2_test(new) # Print result for checking

remove_line_num("test4.txt", "test5.txt")

