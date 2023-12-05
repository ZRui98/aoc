import re
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
        m.append((int(source), int(target), int(offset)))
    m.sort(key=lambda x: x[0])
    return m

soil = buildIntervalMap(lines[soilStart + 1:fertilizerStart - 1])
print(soil)
fertilizer = buildIntervalMap(lines[fertilizerStart + 1:waterStart - 1])
water = buildIntervalMap(lines[waterStart + 1:lightStart - 1])
light = buildIntervalMap(lines[lightStart + 1:temperatureStart - 1])
temperature = buildIntervalMap(lines[temperatureStart + 1:humidityStart - 1])
humidity = buildIntervalMap(lines[humidityStart + 1:locationStart - 1])
location = buildIntervalMap(lines[locationStart + 1:])

def getVal(m, v):
    print(m, v)
    for s, e, o in m:
        if s <= v <= (s + o):
            return v - s + e
    return v

a = 1e10
for s in seeds:
    print(s)
    so = getVal(soil, int(s))
    fert = getVal(fertilizer, so)
    wat = getVal(water, fert)
    lig = getVal(light, wat)
    temp = getVal(temperature, lig)
    hum = getVal(humidity, temp)
    loc = getVal(location, hum)
    a = min(a, loc)
    print('ans', a)