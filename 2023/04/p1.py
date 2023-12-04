import re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

ans = 0
for card in lines:
    c = card.split('|')
    w = c[0].split(':')[1]
    winning = set(re.findall(r'\d+', w))
    contains = set(re.findall(r'\d+', c[1]))
    p = len(winning.intersection(contains)) - 1
    if p >= 0:
        ans += 2 ** p
print(ans)
