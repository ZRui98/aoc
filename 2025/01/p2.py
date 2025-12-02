file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

pos = 50
ans = 0

for k in lines:
    dir = k[0]
    count = int(k[1:])
    t_count = count // 100
    count = count % 100
    opos = pos
    if dir == 'L':
        pos -= count
    else:
        pos += count
    if (pos < 0 or pos > 99):
        pos = pos % 100
        # if original pos = 0, don't increment 0 count. Similarly, if pos = 0, also don't count it since it's done elsewhere
        if opos != 0 and pos != 0:
            t_count += 1
    if pos == 0:
        t_count += 1
    ans += t_count

print(ans)