from functools import cache
from collections import deque

file = open('input.txt', 'r')
lines = [line.rstrip().split(':') for line in file]

adj_list = {entry[0]:set(entry[1].strip().split(' ')) for entry in lines}

if 'out' not in adj_list:
    adj_list['out'] = ''

@cache
def backtrack(curr, dac_visited, fft_visited):
    if curr == 'out':
        return 1 if fft_visited and dac_visited else 0
    if curr == 'fft':
        fft_visited = True
    if curr == 'dac':
        dac_visited = True
    ans = 0
    for neighbor in adj_list[curr]:
        ans += backtrack(neighbor, dac_visited, fft_visited)
    return ans

print(backtrack('svr', False, False))