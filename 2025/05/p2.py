import bisect

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

ans = 0

intervals = []

new_i = 0

for i, line in enumerate(lines):
    if '-' in line:
        rge = line.split('-')
        s, e = int(rge[0]), int(rge[1])
        intervals.append((s, e))
    elif line == '':
        new_i = i + 1
        break

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = -1, -1
    merged = []
    for interval in intervals:
        if start == -1:
            start = interval[0]
            end = interval[1]
        else:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
    if start != -1:
        merged.append([start, end])
    return merged

intervals = merge(intervals)

for interval in intervals:
    ans += interval[1] - interval[0] + 1

print(ans)