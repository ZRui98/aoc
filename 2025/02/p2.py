file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

ranges = map(lambda x: x.split('-'), lines[0].split(','))

def does_repeat(x):
    xx = (x+x)[1:-1]
    pos = xx.find(x)
    if pos == -1:
        return
    return x[:pos + 1]

ans = 0

for s, e in ranges:
    si, ei = int(s), int(e)
    for i in range(si, ei+1):
        repeats = does_repeat(str(i))
        if repeats is not None:
            ans += i

print(ans)