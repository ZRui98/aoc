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
visited.add(l)
hmap = {}
for v in visited:
    if v[1] not in hmap:
        hmap[v[1]] = [v[0], v[0]]
    hmap[v[1]][0] = min(hmap[v[1]][0], v[0])
    hmap[v[1]][1] = max(hmap[v[1]][1], v[0])
ans = 0
for k, v in sorted(hmap.items()):
    inside = False
    s = 0
    i = v[0]
    while i < v[1]:
        if (i, k) in visited:
            tmp = i
            if m[tmp][k] == '-':
                inside = not inside
                i += 1
                continue
            i += 1
            while m[i][k] == '|':
                i += 1
            if m[tmp][k] == 'F':
                if m[i][k] in ['J']:
                    inside = not inside
            elif m[tmp][k] == '7':
                if m[i][k] in 'L':
                    inside = not inside
        elif i < v[1] and inside:
                s += 1
        i += 1
    ans += s

print(ans)