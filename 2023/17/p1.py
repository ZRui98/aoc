import heapq
from collections import defaultdict

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
g = [[int(x) for x in line] for line in lines]

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
opts = {'U': ['L', 'R'], 'D': ['L', 'R'], 'L': ['U', 'D'], 'R': ['U', 'D'], 'X': ['D', 'R']}
def dijkstra(grid, start, end):
    dists = defaultdict(lambda: float('inf'))
    dists[(start, 'X')] = 0
    q = [(0, start,'X')]
    while q:
        dist, (i, j), d  = heapq.heappop(q)
        if (i, j) == end:
            return dist
        for k, (di, dj) in [(x, dirs[x]) for x in opts[d]]:
            alt = dist
            for a in range(1, 4):
                ni, nj = i + di * a, j + dj * a
                if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
                    continue
                v = (ni, nj)
                alt += grid[ni][nj]
                if alt < dists[(v, k)]:
                    dists[(v, k)] = alt
                    heapq.heappush(q, (alt, v, k))

print(dijkstra(g, (0, 0), (len(g) - 1, len(g[0]) - 1)))