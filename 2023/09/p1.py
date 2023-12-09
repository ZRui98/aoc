import re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
instructions = lines[0]

def all_same(x):
    return x.count(x[0]) == len(x)

ans = 0
for line in lines:
    pat = list(map(int, re.findall(r'-?\d+', line)))
    iters = [pat]
    while not all_same(pat):
        new_pat = [0] * (len(pat) - 1)
        for i in range(len(new_pat)):
            new_pat[i] = pat[i + 1] - pat[i]
        pat = new_pat
        iters.append(pat)
    a = iters[-1][-1]
    for i in range(len(iters) - 2, -1, -1):
        a = iters[i][-1] + a
    ans += a
print(ans)