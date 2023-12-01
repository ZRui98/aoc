import re
lookup = {'one': 1, 'two': 2, 'three':3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
file = open('input.txt', 'r')
lines = file.readlines()
ans = 0
for line in lines:
    nmatch = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    if len(nmatch) == 0:
        continue
    n1 = lookup[nmatch[0]] if len(nmatch[0]) > 1 else int(nmatch[0])
    n2 = lookup[nmatch[-1]] if len(nmatch[-1]) > 1 else int(nmatch[-1])
    ans += n1 * 10 + n2
print(ans)