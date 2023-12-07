import re
from collections import Counter
file = open('input.txt', 'r')
players = [line.rstrip() for line in file]

def get_rank(hand):
    freq = Counter(hand)
    sortedHand = sorted(freq.items(), key=lambda x: -x[1])
    print(sortedHand)
    if sortedHand[0][1] == 5:
        return 7
    elif sortedHand[0][1] == 4:
        return 6
    elif sortedHand[0][1] == 3:
        if sortedHand[1][1] == 2:
            return 5
        else:
            return 4
    elif sortedHand[0][1] == 2:
        if sortedHand[1][1] == 2:
            return 3
        else:
            return 2
    else:
        return 1

def get_suite(hand):
    r = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    i = 0
    for c in hand:
        i += r[c]
        i *= 100
    return i

sortList = []
for player in players:
    hand, bid = player.split(' ')
    sortList.append((get_rank(hand), get_suite(hand), int(bid)))
sortList.sort()
print(sum([(r + 1) * b[2] for r, b in enumerate(sortList)]))