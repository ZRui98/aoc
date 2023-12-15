import re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

codes = lines[0].split(',')

hm = [dict() for _ in range(257)]
order = [list() for _ in range(257)]


ans = 0
for code in codes:
    label, val = re.split('=|-', code)
    isSet = '=' in code
    lv = 0
    for c in label:
        v = ord(c)
        lv += v
        lv *= 17
        lv %= 256
    if isSet:
        if label not in hm[lv]:
            order[lv].append(label)
        hm[lv][label] = int(val)
    else:
        if label not in hm[lv]:
            continue
        hm[lv].pop(label)
        order[lv].remove(label)

ans = 0
for bn, box in enumerate(order):
    if not box:
        continue
    for i, el in enumerate(box):
        ans += (bn + 1) * (i + 1) * hm[bn][el]

print(ans)