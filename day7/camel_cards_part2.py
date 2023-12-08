from itertools import groupby

strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 1,
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

#copied and reworked from https://github.com/savbell/advent-of-code-one-liners/blob/master/2023/day-07.py
def score(h):
    if len(set(h)) == 1 or len(set(h)) == 2 and 1 in h:
        return 7
    replace = max([c for c in h if h.count(c) == max([h.count(c) for c in h if c != 1])])
    s = sorted([replace if c == 1 else c for c in h])
    if s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        return 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        return 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        return 3
    elif len(set(s)) == 4:
        return 2
    elif len(set(s)) == 5:
        return 1

with open("data/input_7.txt", "r") as file:
    items = file.read().rstrip().split('\n')

hands = [(list(map(lambda x: strengths[x], list(item.split(' ')[0]))), 
            int(item.split(' ')[1]),
            score(list(map(lambda x: strengths[x], list(item.split(' ')[0]))))) for item in items]

hands.sort(key=lambda x: x[2])
ranked_hands = [list(hand) for _, hand in groupby(hands, lambda x: x[2])]
for hand in ranked_hands:
    hand.sort(key=lambda x: x[0])

hands = []
for hand in ranked_hands:
    hands += hand

winnings = 0
for i, hand in enumerate(hands):
    winnings += int(hand[1]) * (i+1)
print(winnings)