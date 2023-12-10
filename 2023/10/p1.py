import re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
m = []
start = None

def get_next(i, j):
    # print(m[i][j])
    if m[i][j] == 'L':
        return [(i-1, j), (i, j+1)]
    if m[i][j] == '-':
        return [(i, j-1), (i, j+1)]
    if m[i][j] == '|':
        return [(i-1, j), (i+1, j)]
    if m[i][j] == '7':
        return [(i, j-1), (i+1, j)]
    if m[i][j] == 'J':
        return [(i-1, j), (i, j-1)]
    if m[i][j] == 'F':
        return [(i+1, j), (i, j+1)]
    return []

ptrs = []
for i, line in enumerate(lines):
    row = []
    for j, c in enumerate(line):
        if c == 'S':
            start = (i, j)
        row.append(c)
    m.append(row)
# print(m)
for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if start in get_next(start[0] + d[0], start[1] + d[1]):
        # print('aaa', get_next(start[0] + d[0], start[1] + d[1]))
        ptrs.append((start[0] + d[0], start[1] + d[1]))
# print(start, ptrs)
l, r = ptrs[0], ptrs[1]
visited = set([start])
p = 1
while l != r:
    visited.add(l)
    visited.add(r)
    options = get_next(l[0], l[1])
    # print(l, r, options, visited)
    if options[0] in visited:
        l = options[1]
    else:
        l = options[0]
    options = get_next(r[0], r[1])
    if options[0] in visited:
        r = options[1]
    else:
        r = options[0]
    p += 1

print(p)

