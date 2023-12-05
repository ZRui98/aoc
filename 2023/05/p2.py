import re, bisect
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

seeds = re.findall(r'\d+', lines[0].split(':')[1])

soilStart = [i for i, line in enumerate(lines) if '-soil' in line][0]
fertilizerStart = [i for i, line in enumerate(lines) if '-fertilizer' in line][0]
waterStart = [i for i, line in enumerate(lines) if '-water' in line][0]
lightStart = [i for i, line in enumerate(lines) if '-light' in line][0]
temperatureStart = [i for i, line in enumerate(lines) if '-temperature' in line][0]
humidityStart = [i for i, line in enumerate(lines) if '-humidity' in line][0]
locationStart = [i for i, line in enumerate(lines) if '-location' in line][0]

def buildIntervalMap(vals):
    m = []
    for val in vals:
        target, source, offset = re.findall(r'\d+', val)
        m.append((int(source), int(target), int(source) + int(offset)))
    m.sort(key=lambda x: x[0])
    return m

soil = buildIntervalMap(lines[soilStart + 1:fertilizerStart - 1])
fertilizer = buildIntervalMap(lines[fertilizerStart + 1:waterStart - 1])
water = buildIntervalMap(lines[waterStart + 1:lightStart - 1])
light = buildIntervalMap(lines[lightStart + 1:temperatureStart - 1])
temperature = buildIntervalMap(lines[temperatureStart + 1:humidityStart - 1])
humidity = buildIntervalMap(lines[humidityStart + 1:locationStart - 1])
location = buildIntervalMap(lines[locationStart + 1:])

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = -1, -1
    ans = []
    for interval in intervals:
        if start == -1:
            start = interval[0]
            end = interval[1]
        else:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                ans.append([start, end])
                start = interval[0]
                end = interval[1]
    if start != -1:
        ans.append([start, end])
    return ans

def getUniq(m, i, j):
    x = i
    ans = []
    while x < j:
        ip = bisect.bisect_left(m, x + 1, key=lambda x: x[0]) - 1 # get greatest interval with start <= x
        if ip == -1:
            ans.append([x, m[0][0]])
            x = m[0][0]
            continue
        s, e, o = m[ip]
        if s <= x < o: # if x is in range, everything from x to o will be the same #
            nx = min(o, j)
            ans.append([x-s+e, nx-s+e])
            x = o
        elif x >= o: # if x is greater than the end of the closest left range, the numbers x - m[ip + 1][0] - 1 (start of range greater than x) will map each to a different number, so put in a range
            if ip + 1 == len(m):
                ans.append([x, j])
                x = j
            else:
                nx = min(j, m[ip + 1][0])
                ans.append([x, nx])
                x = nx
    return ans

sints = []
for i in range(0, len(seeds), 2):
    s = int(seeds[i])
    e = s + int(seeds[i + 1])
    sints.append([s,e])
soints = []
for sis, sie in sints:
    soints += getUniq(soil, sis, sie)
fertints = []
for sois, soie in soints:
    fertints += getUniq(fertilizer, sois, soie)
wints = []
for fis, fie in fertints:
    wints += getUniq(water, fis, fie)
lints = []
for wis, wie in wints:
    lints += getUniq(light, wis, wie)
tints = []
for lis, lie in lints:
    tints += getUniq(temperature, lis, lie)
hints = []
for tis, tie in tints:
    hints += getUniq(humidity, tis, tie)
loints = []
for his, hie in hints:
    loints += getUniq(location, his, hie)
    
print('ans', min(x[0] for x in merge(loints)))