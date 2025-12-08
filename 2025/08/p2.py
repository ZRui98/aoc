import math
from collections import deque

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

dists.sort()
dists = deque(dists)
last = None

while dists and max(rank) < len(boxes):
    _, i, j = dists.popleft()
    joined = union(i, j)
    if joined:
        last = (i, j)

print(boxes[last[0]][0] * boxes[last[1]][0])