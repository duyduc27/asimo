# mymodule1.py

myage = 28
year = 2019

print("My name is", __name__)

if __name__ == "__main__":
    print("This won't run if I'm  imported.")

# Only print if this one is the currently module caller
# The namespace_test didn't show up this print if module 1 was imported

