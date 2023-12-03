file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
L = len(lines[0])
ans = 0
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '*':
            continue
        used = set()
        nums = []
        for d in dirs:
            x, y = j + d[1], i + d[0]
            if y * L + x in used:
                continue
            if '0' <= lines[y][x] <= '9':
                l, r = x, x
                used.add(y * L + x)
                while l - 1 >= 0 and '0' <= lines[y][l - 1] <= '9':
                    l -= 1
                    used.add(y * L + l)
                while r + 1 < len(lines[y]) and '0' <= lines[y][r + 1] <= '9':
                    r += 1
                    used.add(y * L + r)
                # print(line[l:r + 1])
                nums.append(int(lines[y][l:r + 1]))
        if len(nums) == 2:
            ans += nums[0] * nums[1]
                
print(ans)
        