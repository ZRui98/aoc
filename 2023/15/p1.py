file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

codes = lines[0].split(',')

ans = 0
for code in codes:
    cv = 0
    for c in code:
        v = ord(c)
        cv += v
        cv *= 17
        cv %= 256
    ans += cv
print(ans)
