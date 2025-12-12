# i kneel https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/

from collections import deque
from functools import cache

file = open('input.txt', 'r')
lines = [line.rstrip().split() for line in file]

# machine[0] = state
# machine[1] = buttons
# machine[2] = joltage
machines = [(tuple(map(lambda x: x == '#', line[0][1:-1])), tuple([tuple(int(x) for x in action[1:-1].split(',')) for action in line[1:-1]]), tuple(int(x) for x in line[-1][1:-1].split(','))) for line in lines]

def backtrack(desired, actions):
    ans = set()
    def backtrack(current, i, state):
        if i >= len(actions):
            #print(current, i, state)
            if tuple(i % 2 for i in current) == desired:
                ans.add((current, len(state)))
            return
        backtrack(current, i + 1, state)
        take_action = list(current)
        for a in actions[i]:
            take_action[a] = (current[a] + 1)
        backtrack(tuple(take_action), i + 1, state + [i])

    backtrack(tuple(0 for _ in range(len(desired))), 0, [])
    return ans
            

def solve(desired, actions):
    @cache
    def solve(desired):
        ans = 100000
        uneven = tuple(desired[i] % 2 for i in range(len(desired)))
        possibilities = backtrack(uneven, actions)
        for possibility, steps in possibilities:
            if any([possibility[x] > desired[x] for x in range(len(desired))]):
                continue
            leftovers = tuple((desired[x] - possibility[x]) // 2 for x in range(len(desired)))
            #print('leftovers', desired, uneven, leftovers, tuple((desired[x] - uneven[x]) for x in range(len(desired))))
            if all([leftover == 0 for leftover in leftovers]):
                ans = min(ans, steps)
                continue
            ans = min(ans, steps + (2 * solve(leftovers)))
        return ans
    return solve(desired)

ans = 0
for machine in machines:
    presses = solve(machine[2], machine[1])
    ans += presses
print(ans)