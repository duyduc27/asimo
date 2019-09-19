class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other): # compare
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0

    def __eq__(self, other): # equal
        return self.cmp(other) == 0
    def __le__(self, other): # less than and equal
        return self.cmp(other) <= 0
    def __ge__(self, other): # greater than and equal
        return self.cmp(other) >= 0
    def __gt__(self, other): # greater than
        return self.cmp(other) > 0
    def __lt__(self, other): # less than
        return self.cmp(other) < 0
    def __ne__(self, other): # no equal
        return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " "*i + str(self.cards[i]) + "\n"
        return s
    
    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()
    
    def is_empty(self):
        return self.cards == []
    
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def deal(self, hands, num_cards=9999):

        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break         # Break if out of cards
            card = self.pop() # Take the top card
            hand = hands[i % num_hands] # Whose turn is next?
            hand.add(card)    # Add the card to the hand

    
class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name
    
    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)
    

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3- card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matched {2}".
                format(self.name, card, match))
                count += 1
        return count

class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
        
        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn+1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        
        return count
    
    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count
    
    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        for hand in self.hands:
            print(hand)