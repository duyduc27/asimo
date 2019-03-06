def text_to_words(the_text):
    """ return a list of words with all punctuation removed
    and all in lowercase """
    my_substitutions = the_text.maketrans(
    # If you find any of these
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
    # Replace them by these
    "abcdefghijklmnopqrstuvwxyz                                          ")
    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of words """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("AliceInWonderland.txt")
book_words.sort() # Make order at this words list

def make_dic(lis):
    """ make dictionary from a list """
    dic = {} # Set initial dic
    for i in lis:
        dic[i] = dic.get(i, 0) + 1
    return dic

book_dic = make_dic(book_words)

def write_new_file(filename, dic):
    """ Write results from dic into new file """
    layout = "{0:<15}{1:>15}"
    f = open(filename, "w")
    f.write("Word              Count\n")
    f.write("=======================\n")
    for k, v in dic.items():
        content = layout.format(k, dic[k])
        f.write(content + "\n")
    f.close()

write_new_file("alice_words.txt", book_dic)

def analyse_dic(dic): # For testing
    """ Statics the dictionary """
    longest_wd = None
    length = 0
    ct = 0
    layout = "{0:<10}{1:>10}"
    print("Word              Count")
    print("=======================")
    for k, v in dic.items():
        ct += 1
        if ct < 10: # Because I don't want to print all list
            print(layout.format(k, dic[k]))
    for k in dic.keys():
        if len(k) > length:
            length = len(k)
            longest_wd = k
    print("The longest word in Alice in Wonderland is: ", longest_wd, ". It has", length, "characters.")

analyse_dic(book_dic)
print("The word 'alice' occurred in", book_dic["alice"], "times.")