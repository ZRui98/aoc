file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

M = len(lines)
load = 0
for j in range(len(lines[0])):
    unmovable = -1
    for i, line in enumerate(lines):
        if line[j] == '.':
            continue
        elif line[j] == 'O':
            unmovable += 1
            load += M - unmovable
        else:
            unmovable = i

print(load)