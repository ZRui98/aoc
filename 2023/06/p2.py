import re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
times = [int(v) for v in re.findall(r'\d+', lines[0])]
distances = [int(v) for v in re.findall(r'\d+', lines[1])]
ans = 0
for race in zip(times, distances):
    for i in range(1, race[0]):
        maxDist = i * (race[0] - i)
        if maxDist > race[1]:
            ans += 1
print(ans)