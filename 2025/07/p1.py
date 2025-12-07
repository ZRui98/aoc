file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
beams = set(j for j in range(len(lines[0])) if lines[0][j] == 'S')

splits = 0

for line in lines[1:]:
    newbeams = set()
    for beam in beams:
        if line[beam] == '^':
            newbeams.add(beam - 1)
            newbeams.add(beam + 1)
            splits += 1
        else:
            newbeams.add(beam)
    beams = newbeams

print(splits)