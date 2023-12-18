file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
g = [line.split(' ') for line in lines]

verts = []
y, x, b = 0, 0, 0
for line in lines:
    d, dist, _ = line.split(' ')
    val = int(dist)
    verts.append((y, x))
    if d == 'U':
        y -= val
    elif d == 'D':
        y += val
    elif d == 'L':
        x -= val
    else:
        x += val
    b += val
verts.append((0, 0))
sum1, sum2 = 0, 0

for i in range(len(verts) - 1):
    sum1 += verts[i][0] * verts[i + 1][1]
    sum2 += verts[i][1] * verts[i + 1][0]
print(abs(sum1 - sum2) / 2 + 1 - b/2 + b)