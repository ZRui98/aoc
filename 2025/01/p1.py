file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

pos = 50
ans = 0

for k in lines:
    dir = k[0]
    count = int(k[1:])
    if dir == 'L':
        pos -= count
    else:
        pos += count
    pos = pos % 100
    print(pos, ans)
    if pos == 0:
        ans += 1

print(ans)