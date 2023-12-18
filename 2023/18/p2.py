file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
g = [line.split(' ') for line in lines]

verts = []
y, x, b = 0, 0, 0
for line in lines:
    hex = line.split(' ')[-1].strip('()')
    print(hex)
    val = int(hex[1:-1], 16)
    d = hex[-1]
    verts.append((y, x))
    if d == '0':
        x += val
    elif d == '1':
        y += val
    elif d == '2':
        x -= val
    else:
        y -= val
    b += val
verts.append((0, 0))
sum1, sum2 = 0, 0

for i in range(len(verts) - 1):
    sum1 += verts[i][0] * verts[i + 1][1]
    sum2 += verts[i][1] * verts[i + 1][0]
print(abs(sum1 - sum2) / 2 + 1 - b/2 + b)