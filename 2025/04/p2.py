file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

file = open('input.txt', 'r')
lines = [list(line.rstrip()) for line in file]

def can_go_to(i, j):
    total_paper = 0
    for y in range(-1, 2):
        for x in range (-1, 2):
            ii = i + y
            jj = j + x
            if ii < 0 or jj < 0 or ii >= len(lines) or jj >= len(lines[0]):
                continue
            if ii == i and jj == j:
                continue
            if lines[ii][jj] == '@':
                total_paper += 1
    return total_paper  < 4

ans = 0

add = -1
while add != 0:
    add = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '@':
                if can_go_to(i, j):
                    lines[i][j] = 'x'
                    add += 1
    ans += add


print(ans)