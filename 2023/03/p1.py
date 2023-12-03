file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

def is_symbol(c):
    if '0' <= c <= '9':
        return False
    if c == '.':
        return False
    return True

def has_symbol(y, l, r):
    if y > 0:
        for i in range(max(0, l - 1), min(len(lines[y - 1]), r + 2)):
            if is_symbol(lines[y - 1][i]):
                return True
    if l - 1 >= 0 and is_symbol(lines[y][l - 1]):
        return True
    if r + 1 < len(lines[y]) and is_symbol(lines[y][r + 1]):
        return True
    if y < len(lines) - 1:
        for i in range(max(0, l - 1), min(len(lines[y + 1]), r + 2)):
            if is_symbol(lines[y + 1][i]):
                return True

ans = 0
for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        c = line[j]
        if c > '9' or c < '0':
            j += 1
            continue
        r = j
        while r < len(line) and '0' <= line[r] <='9':
            r += 1
        if has_symbol(i, j, r - 1):
            # print(line[j:r])
            ans += int(line[j:r])
        j = max(r, j + 1)
print(ans)
        