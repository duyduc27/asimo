data = "ThiS is String with Upper and lower case Letters"
def analyse_dt(dt):
    """ initialize processing data """
    dic = {} # Set initial dic

    # Initialize processing data
    n= dt.lower()
    n1 = "".join(n.split())
    for letter in n1:
        dic[letter] = dic.get(letter, 0) + 1

    # Access dic and turn it to a order list
    m = list(dic.items()) # Turn dic to list
    m.sort() # Make order
    for i in m:
        print(i[0], i[1]) # Print result of each elements

analyse_dt(data)
