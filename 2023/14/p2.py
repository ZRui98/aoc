file = open('input.txt', 'r')
lines = [list(line.rstrip()) for line in file]

def rotate(mat):
    return [list(x) for x in list(zip(*mat[::-1]))]

def key(mat):
    return ''.join([x for row in mat for x in row])

def cycle(mat):
    for _ in range(4):
        for j in range(len(mat[0])):
            unmovable = -1
            for i, line in enumerate(mat):
                if line[j] == 'O':
                    unmovable += 1
                    tmp = mat[unmovable][j]
                    mat[unmovable][j] = mat[i][j]
                    mat[i][j] = tmp
                elif line[j] == '#':
                    unmovable = i
        mat = rotate(mat)
    s = 0
    M = len(mat)
    for j in range(len(mat[0])):
        for i, line in enumerate(mat):
            if line[j] == 'O':
                s += len(mat) - i
    return s, mat

seen = {}
scores = []

mat = lines
while True:
    score, mat = cycle(mat)
    k = key(mat)
    if k in seen:
        cl = len(seen) - seen[k]
        cs = seen[k]
        print(scores[(1000000000 - cs - 1) % cl + cs])
        break
    seen[k] = len(scores)
    scores.append(score)