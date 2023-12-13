file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

puzzles = []
tmp = []
for line in lines:
    if not line.strip():
        puzzles.append(tmp)
        tmp = []
    else:
        tmp.append(list(line))

def findReflection(puzzle):
    # vertical lines
    for i in range(len(puzzle[0]) - 1):
        valid = True
        smudge = 0
        l, r = i, i + 1
        while l >= 0 and r < len(puzzle[0]):
            for line in puzzle:
                if line[l] != line[r]:
                    smudge += 1
                    if smudge >= 2:
                        valid = False
                        break
                pass
            if not valid:
                break
            r += 1
            l -= 1
        if valid and smudge == 1:
            return (i, -1)

    smudge = 0
    # horizontal lines
    for i in range(len(puzzle) - 1):
        smudge = 0
        valid = True
        l, r = i, i + 1
        while l >= 0 and r < len(puzzle):
            for j in range(len(puzzle[0])):
                if puzzle[l][j] != puzzle[r][j]:
                    smudge += 1
                    if smudge >= 2:
                        valid = False
                        break
                pass
            if not valid:
                break
            r += 1
            l -= 1
        if valid and smudge == 1:
            return (-1, i)
    return -1, -1
            
ans = 0
for puzzle in puzzles:
    v, h = findReflection(puzzle)
    print(v + 1, h + 1)
    if v >= 0:
        ans += v + 1
    elif h >= 0:
        ans += (h + 1) * 100

print(ans)