file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

rows = set()
cols = set()
stars = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            rows.add(i)
            cols.add(j)
            stars.append((i, j))

ans = 0
e = 1e6
for i, s in enumerate(stars):
    for j in range(i + 1, len(stars)):
        destY, destX = s
        currY, currX = stars[j]
        distY, distX = 0, 0
        while destX != currX or destY != currY:
            if currY < destY:
                currY += 1 
                if currY in rows:
                    distY += e
                else:
                    distY += 1 
            elif currY > destY:
                currY -= 1
                if currY not in rows:
                    distY += e
                else:
                    distY += 1

            if currX < destX:
                currX += 1 
                if currX not in cols:
                    distX += e
                else:
                    distX += 1 
            elif currX > destX:
                currX -= 1
                if currX not in cols:
                    distX += e
                else:
                    distX += 1
        dist = distY + distX
        ans += dist
        # print(s, stars[j], dist, distX, distY, currY, currX)
print(ans)