from collections import deque

file = open('input.txt', 'r')
lines = [line.rstrip().split() for line in file]


# machine[0] = state
# machine[1] = buttons
# machine[2] = joltage
machines = [(tuple(map(lambda x: x == '#', line[0][1:-1])), tuple([tuple(int(x) for x in action[1:-1].split(',')) for action in line[1:-1]]), tuple(line[-1][1:-1].split(','))) for line in lines]

def bfs(machine):
    visited = set()
    initial = tuple(False for _ in range(len(machine[0])))
    presses = 1
    q = deque([initial])
    while q:
        new_q = deque()
        while q:
            current = q.popleft()
            for action in machine[1]:
                new_state = list(current)
                for button in action:
                    new_state[button] = not new_state[button]
                new_state = tuple(new_state)
                if new_state == machine[0]:
                    return presses
                if new_state in visited:
                    continue
                visited.add(new_state)
                new_q.append(new_state)
        q = new_q
        presses += 1
    return -1

ans = 0

for machine in machines:
    presses = bfs(machine)
    ans += presses

print(ans)