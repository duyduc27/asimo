# Exercise 13.11.1
def reverse(old, new):
    """ Reverse lines of old file into new file """
    infile = open(old, "r")
    xs = infile.readlines() # Turn lines of old file into a list
    infile.close()

    xs.reverse() # Reverse this list
    outfile = open(new, "w")
    for i in xs:
        outfile.write(i) # Write a line-at-a-time at reversed list
    outfile.close()


reverse("test1.txt", "test2.txt")



