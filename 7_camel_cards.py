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

if __name__=="__main__":

    with open("data/test.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    
    #part 1
    hands = [Hand(list(map(lambda x: strengths[x], list(item.split(' ')[0]))), 
                int(item.split(' ')[1])) for item in items]
    
    hands_sorted = sorted(hands, key = lambda hand: (assign_hand_type(hand.cards).value, hand.cards))

    winnings = [rank * hand.bid for rank, hand in enumerate(hands_sorted, start = 1)]

    # print(sum(winnings))

    #part 2
    '''
    I haven't managed to solve this part on a first day, I think I have overengineered the first part and had gone into problems
    resolving edge cases in a 2nd part. I would rework this one and attempt it once again from beginning.
    '''
    # for i in range(0, len(hands)):
    #     temp = []
    #     temp_tracker = []
    #     if 11 in hands[i].cards:
    #         for value in strengths.values():
    #             # to_replace = value
    #             # temp.append(list(map(lambda x: value if x == 11 else x, hands[i].cards)))
    #             temp_2 = []
    #             temp_2_tracker = []
    #             for j in range(0, len(hands[i].cards)):
    #                 if hands[i].cards[j] == 11:
    #                     temp_2.append(value)
    #                     temp_2_tracker.append(True)
    #                 else:
    #                     temp_2.append(hands[i].cards[j])
    #                     temp_2_tracker.append(False)
    #             temp.append(temp_2)
    #             temp_tracker.append(temp_2_tracker)
    #         # hands[i] = Hand(max(temp, key = lambda temp: assign_hand_type(temp).value), hands[i].bid)
    #         # print(max(temp, key = lambda temp: assign_hand_type(temp).value), hands[i].bid)
    #         temp_2 = max(temp, key = lambda temp: assign_hand_type(temp).value)
    #         for j in range(0, len(temp)):
    #             if temp[j] == temp_2:
    #                 temp_2_tracker = temp_tracker[j]
    #                 break
    #         print(temp_2, temp_2_tracker, hands[i].bid)
    #         for j in range(0, len(temp_2)):
    #             if temp_2_tracker[j]:
    #                 temp_2 = list(map(lambda x: 1 if x == temp_2[j] else x, temp_2))
    #                 # temp_2[j] = 1
    #         hands[i] = Hand(temp_2, hands[i].bid)
    #         # print(max(temp, key = lambda temp: assign_hand_type(temp).value), hands[i].bid)

    # hands_sorted = sorted(hands, key = lambda hand: (assign_hand_type(hand.cards).value, hand.cards))

    # winnings = [rank * hand.bid for rank, hand in enumerate(hands_sorted, start = 1)]

    # for hands in hands_sorted:
    #     print(hands.cards, hands.bid)


    


