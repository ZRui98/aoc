file = open('input.txt', 'r')
pts = [[int(x) for x in line.rstrip().split(',')] for line in file]
area = 0
for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        s1 = abs(pts[i][0] - pts[j][0]) + 1
        s2 = abs(pts[i][1] - pts[j][1]) + 1
        area = max(s1 * s2, area)

print(area)