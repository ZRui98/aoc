import re
from collections import Counter
from math import gcd
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
instructions = lines[0]

directions = {}
for line in lines[2:]:
    node, dirs = line.split(' = ')
    l, r = dirs.strip('()').split(', ')
    directions[node] = (l, r)

locs = [x for x in directions.keys() if x[-1] == 'A']
a = []
for loc in locs:
    steps = 0
    l = loc
    while l[-1] != 'Z':
        d = instructions[steps % len(instructions)]
        if d == 'L':
            l = directions[l][0]
        else:
            l =directions[l][1]
        steps += 1
    a.append(steps)
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)