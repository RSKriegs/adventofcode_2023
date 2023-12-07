from collections import namedtuple, Counter
from enum import Enum, auto

Hand = namedtuple('Hand',('cards', 'bid'))

class Hand_Type(Enum):
    high_card       = auto()
    one_pair        = auto()
    two_pair        = auto()
    three_of_a_kind = auto()
    full_house      = auto()
    four_of_a_kind  = auto()
    five_of_a_kind  = auto()

def assign_hand_type(cards):
    counts = sorted(Counter(cards).values(), reverse = True)
    if counts == [5]:
        return Hand_Type.five_of_a_kind
    elif counts == [4, 1]:
        return Hand_Type.four_of_a_kind
    elif counts == [3, 2]:
        return Hand_Type.full_house
    elif counts == [3, 1, 1]:
        return Hand_Type.three_of_a_kind
    elif counts == [2, 2, 1]:
        return Hand_Type.two_pair
    elif counts == [2, 1, 1, 1]:
        return Hand_Type.one_pair
    elif counts == [1, 1, 1, 1, 1]:
        return Hand_Type.high_card

strengths = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

if __name__=="__main__":

    with open("data/input_7.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    hands = [Hand(list(map(lambda x: strengths[x], list(item.split(' ')[0]))), 
                int(item.split(' ')[1])) for item in items]
    
    hands = sorted(hands, key = lambda hand: (assign_hand_type(hand.cards).value, hand.cards))

    winnings = [rank * hand.bid for rank, hand in enumerate(hands, start = 1)]

    print(sum(winnings))

