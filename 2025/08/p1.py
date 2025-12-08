import math
import heapq

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

boxes = []

for line in lines:
    line = line.split(',')
    boxes.append((int(line[0]), int(line[1]), int(line[2])))


dists = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dists.append((math.dist(boxes[i], boxes[j]), i, j))

M = len(boxes)
prev = [i for i in range(M)]
rank = [1] * M

def find(x):
    p = prev[x]
    while prev[p] != p:
        prev[p] = prev[prev[p]]
        p = prev[p]
    return p

def union(x, y):
    xp, yp = find(x), find(y)
    if xp == yp:
        return False
    if rank[xp] > rank[yp]:
        prev[yp] = xp
        rank[xp] += rank[yp]
    else:
        prev[xp] = yp
        rank[yp] += rank[xp]
    return True

heapq.heapify(dists)

N = 1000

for x in range(N):
    _, i, j = heapq.heappop(dists)
    union(i, j)

rank.sort(key= lambda x: -x)

total = 1
for i in range(3):
    total *= rank[i]

print(total)