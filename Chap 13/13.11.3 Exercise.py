# Exercise 13.11.3
from read2test import read_2_test # Import a small module for reading text
def number_lines(old, new, num):
    """ Create a new copy file with first n lines have to numbered """
    infile = open(old, "r")
    xs = infile.readlines() # Turn all lines of old file into a list
    infile.close()


    outfile = open(new, "w")
    for i in range(num):  # Loop to get first n elements
        s = "{0:04d} ".format(i+1)+ xs[i] # Number their line by a 4 digit number
        outfile.write(s)

    for i in xs[num:]: # Get the rest elements
        outfile.write(i)

    outfile.close()
    read_2_test(new) # Print result for checking


number_lines("test3.txt", "test4.txt", 5)

