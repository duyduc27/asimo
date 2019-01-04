def read_2_test(file):
    """ Print file for reading """
    f = open(file, "r")
    file_handle = f.readlines() # Turn all lines of file into list
    for i in file_handle:
        print(i, end="")
