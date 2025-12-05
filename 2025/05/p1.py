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

for i in range(new_i, len(lines)):
    x = int(lines[i])
    interval_i = bisect.bisect_right(intervals, x, key=lambda x: x[0]) - 1
    if interval_i < 0:
        continue
    interval = intervals[interval_i]
    if interval[0] <= x <= interval[1]:
        ans += 1

print(ans)