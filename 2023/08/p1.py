import re
from collections import Counter
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
instructions = lines[0]

directions = {}
for line in lines[2:]:
    node, dirs = line.split(' = ')
    l, r = dirs.strip('()').split(', ')
    directions[node] = (l, r)

loc = 'AAA'
steps = 0
while loc != 'ZZZ':
    d = instructions[steps % len(instructions)]
    if d == 'L':
        loc = directions[loc][0]
    else:
        loc =directions[loc][1]
    steps += 1
print(steps)