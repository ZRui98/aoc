file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

ranges = map(lambda x: x.split('-'), lines[0].split(','))

def does_repeat(x):
    mid = len(x) // 2
    return x[:mid] == x[mid:]

ans = 0

for s, e in ranges:
    si, ei = int(s), int(e)
    for i in range(si, ei+1):
        repeats = does_repeat(str(i))
        if repeats:
            ans += i

print(ans)