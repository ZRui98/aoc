from collections import deque
file = open('input.txt', 'r')
grid = [line.rstrip() for line in file]

lights = deque([(0, 0, 'R')])
energized = set()
visited = set()

def outside(i, j):
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) 

while lights:
    i, j, d = lights.popleft()
    if (i, j, d) in visited:
        continue
    visited.add((i, j, d))
    energized.add((i, j))
    if grid[i][j] == '\\':
        if d == 'U' and not outside(i, j - 1):
            lights.append((i, j - 1, 'L'))
        elif d == 'L' and not outside(i - 1, j):
            lights.append((i - 1, j, 'U'))
        elif d == 'R' and not outside(i + 1, j):
            lights.append((i + 1, j, 'D'))
        elif d == 'D' and not outside(i, j + 1):
            lights.append((i, j + 1, 'R'))
    elif grid[i][j] == '/':
        if d == 'U' and not outside(i, j + 1):
            lights.append((i, j + 1, 'R'))
        elif d == 'R' and not outside(i - 1, j):
            lights.append((i - 1, j, 'U'))
        elif d == 'L' and not outside(i + 1, j):
            lights.append((i + 1, j, 'D'))
        elif d == 'D' and not outside(i, j - 1):
            lights.append((i, j - 1, 'L'))
    elif grid[i][j] == '|':
        if d == 'U' and not outside(i - 1, j):
            lights.append((i - 1, j , 'U'))
        elif d == 'D' and not outside(i + 1, j):
            lights.append((i + 1, j, 'D'))
        elif d == 'L' or d == 'R':
            if not outside(i + 1, j):
                lights.append((i + 1, j, 'D'))
            if not outside(i - 1, j):
                lights.append((i - 1, j, 'U'))
    elif grid[i][j] == '-':
        if d == 'L' and not outside(i, j - 1):
            lights.append((i, j - 1, 'L'))
        elif d == 'R' and not outside(i, j + 1):
            lights.append((i, j + 1, 'R'))
        elif d == 'U' or d == 'D':
            if not outside(i, j + 1):
                lights.append((i, j + 1, 'R'))
            if not outside(i, j - 1):
                lights.append((i, j - 1, 'L'))
    else:
        if d == 'U' and not outside(i - 1, j):
            lights.append((i - 1, j, 'U'))
        elif d == 'L' and not outside(i, j - 1):
            lights.append((i, j - 1, 'L'))
        elif d == 'R' and not outside(i, j + 1):
            lights.append((i, j + 1, 'R'))
        elif d == 'D' and not outside(i + 1, j):
            lights.append((i + 1, j, 'D'))

print(len(energized))