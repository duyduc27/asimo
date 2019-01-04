# Exercise 13.11.2
def find_specify_wlines(sub, file):
    """ Read and print only those lines that contain specify substring"""
    f = open(file, "r")
    while True:
        theline = f.readline() # Read a line-at-a-time
        if len(theline) == 0: # Failed to read, then exit loop
            break
        elif theline.find(sub) != -1:
            print(theline, end="") # Prevent Python add newline char

print("""***Test with "Snake Eater' song from Metal Gear Solid 3: Snake Eater Original***""")
# http://y2u.be/I8pg2XoQTlA
find_specify_wlines("Snake", "Cynthia-harrell-snake-eater-lyrics.txt")