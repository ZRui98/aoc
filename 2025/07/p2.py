from collections import defaultdict

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
beams = defaultdict(int, {j: 1 for j in range(len(lines[0])) if lines[0][j] == 'S'})

for line in lines[1:]:
    newbeams = defaultdict(int)
    for beam in beams.keys():
        if line[beam] == '^':
            newbeams[beam + 1] += beams[beam]
            newbeams[beam - 1] += beams[beam]
        else:
            newbeams[beam] += beams[beam]

    beams = newbeams

print(sum(beams.values()))