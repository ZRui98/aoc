from functools import cache

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

seq = []
s = []

def isValid(i, sIdx, cnt):
    if sIdx == len(s):
        return True if cnt == 0 else False
    return False

@cache
def solve(i, sIdx, cnt):
    m = 0 if sIdx >= len(s) else s[sIdx]
    if i == len(seq):
        return 1 if isValid(i, sIdx, cnt) else 0
    if seq[i] == '#':
        return solve(i + 1, sIdx, cnt + 1)
    elif seq[i] == '.':
        if i > 0 and seq[i - 1] == '#':
            if cnt < m or cnt > m:
                return 0
            sIdx += 1
        return solve(i + 1, sIdx, 0)
    else:
        seq[i] = '#'
        a = solve(i + 1, sIdx, cnt + 1)
        seq[i] = '.'
        b = -1
        if i > 0 and seq[i - 1] == '#':
            if cnt < m or cnt > m:
                b = 0
            sIdx += 1
        if b < 0:
            b = solve(i + 1, sIdx, 0)
        seq[i] = '?'
        return a + b

ans = 0
for line in lines:
    tmp1, tmp2 = line.split(' ')
    ts = list(tmp1)
    seq = []
    for i in range(5):
        seq += ts
        seq.append('?')
    seq.pop()
    s = []
    ts = [int(x) for x in tmp2.split(',')]
    for i in range(5):
        s += ts
    seq = list(''.join(seq).strip('.'))
    seq += ['.', '.']
    a = solve(0, 0, 0)
    solve.cache_clear()
    ans += a
print(ans)