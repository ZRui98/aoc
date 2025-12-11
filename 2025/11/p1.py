from functools import cache
from collections import deque

file = open('input.txt', 'r')
lines = [line.rstrip().split(':') for line in file]

adj_list = {entry[0]:set(entry[1].strip().split(' ')) for entry in lines}

@cache
def backtrack(curr):
    if curr == 'out':
        return 1
    ans = 0
    for neighbor in adj_list[curr]:
        ans += backtrack(neighbor)
    return ans

print(backtrack('you'))