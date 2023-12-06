import re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
times = [int(v) for v in re.findall(r'\d+', lines[0])]
distances = [int(v) for v in re.findall(r'\d+', lines[1])]
ans = 1
for race in zip(times, distances):
    a = 0
    for i in range(1, race[0]):
        maxDist = i * (race[0] - i)
        if maxDist > race[1]:
            a += 1
    ans *= a
print(ans)