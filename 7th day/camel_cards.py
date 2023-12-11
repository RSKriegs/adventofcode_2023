from collections import namedtuple, Counter
from itertools import groupby
from enum import Enum, auto

Hand = namedtuple('Hand',('cards', 'bid'))
Hand_2 = namedtuple('Hand',('cards', 'bid', 'dummy'))

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
    
def assign_hand_type_2(cards):
    counts = sorted(Counter(cards).values(), reverse = True)
    if counts == [5]:
        return 7
    replace = max([card for card in cards if cards.count(card) == max([cards.count(card) for card in cards if card != 2])])
    cards = sorted([replace if card == 2 else card for card in cards])
    counts = sorted(Counter(cards).values(), reverse = True)
    if counts == [4, 1]:
        return 6
    elif counts == [3, 2]:
        return 5
    elif counts == [3, 1, 1]:
        return 4
    elif counts == [2, 2, 1]:
        return 3
    elif counts == [2, 1, 1, 1]:
        return 2
    elif counts == [1, 1, 1, 1, 1]:
        return 1
    else:
        return 7

strengths = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2  
}

strengths_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 2,
    "T": 11,
    "9": 10,
    "8": 9,
    "7": 8,
    "6": 7,
    "5": 6,
    "4": 5,
    "3": 4,
    "2": 3  
}

if __name__=="__main__":

    with open("data/input_7.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    
    #part 1
    hands = [Hand(list(map(lambda x: strengths[x], list(item.split(' ')[0]))), 
                int(item.split(' ')[1])) for item in items]
    
    hands_sorted = sorted(hands, key = lambda hand: (assign_hand_type(hand.cards).value, hand.cards))

    winnings = [rank * hand.bid for rank, hand in enumerate(hands_sorted, start = 1)]

    #part 2
    hands = [Hand_2(list(map(lambda x: strengths_2[x], list(item.split(' ')[0]))), 
            int(item.split(' ')[1]),
            assign_hand_type_2(list(map(lambda x: strengths_2[x], list(item.split(' ')[0]))))) for item in items]
    
    ranked_hands = [list(hand) for _, hand in groupby(sorted(hands, key=lambda x: x[2]), lambda x: x[2])]

    hands = []
    winnings = 0
    for hand in ranked_hands:
        hands += sorted(hand, key=lambda x: x[0])
    for i, hand in enumerate(hands):
        winnings += int(hand[1]) * (i+1)
    print(winnings)