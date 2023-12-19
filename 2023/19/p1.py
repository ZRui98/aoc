import json, re
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

workflows = {}

i = 0
for line in lines:
    if not line:
        break
    start = line.find('{')
    name = line[:start]
    rules = line[start + 1: -1].split(',')
    lang = []
    for x in range(len(rules) - 1):
        stmt, res = rules[x].split(':')
        lang.append((stmt, res))
    lang.append(('True', rules[-1]))
    workflows[name] = lang
    i += 1

ans = 0
for line in lines[i + 1:]:
    js = re.sub(r"(\w+):", r'"\1":',  re.sub("=", ":",line))
    v = json.loads(js)
    x, m, a, s = int(v['x']), int(v['m']), int(v['a']), int(v['s'])
    workflow = 'in'
    while workflow in workflows:
        for rule in workflows[workflow]:
            if eval(rule[0]):
                workflow = rule[1]
                break
    if workflow == 'A':
        ans += x + m + a + s
    
print(ans)