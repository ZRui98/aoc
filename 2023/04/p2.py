import re
from collections import defaultdict
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

ans = 0
win = set()
wc = defaultdict(int)
for i, card in enumerate(lines):
    c = card.split('|')
    w = c[0].split(':')[1]
    winning = set(re.findall(r'\d+', w))
    contains = set(re.findall(r'\d+', c[1]))
    p = len(winning.intersection(contains))
    if p >= 1:
        win.add(i)
        wc[i] = p
cnt = [1] * len(lines)
for i in range(len(lines)):
    if i in win:
        for w in range(i + 1, i + 1 + wc[i]):
            cnt[w] += cnt[i]

print(sum(cnt))
