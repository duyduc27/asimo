# Exercise 7.26.17
# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

def main_one():
    round_game = 0 # Set initial values for counter variables
    win = 0
    drawn = 0
    lose = 0
    """
    Make a while loop. Player can play how many rounds as they want.
    The program will terminate if their input is NOT "y"
    """
    while True:
        round_game += 1
        a = play_once(True) # Human play first
        if a == -1:
            print("human won")
            win += 1
        elif a == 0:
            print("game drawn")
            drawn += 1
        elif a == 1:
            print("computer won")
            lose += 1
        ratio = round(win/round_game*100,2) # Ratio between win and total games
                                            # Precision 2 digits of float number

        print("won", win, " drawn", drawn, " losed", lose, ". Total games:", round_game)
        print("your win rate is", ratio, "percent")
        print() # Seprate information each round by a newline

        i = input("Do you want to play again? 'y'")
        if i != "y": # Condition to exit loop
            print("good bye")
            return False # Exit while loop

main_one()
# My flowchart: https://ibb.co/KqggHZZ
