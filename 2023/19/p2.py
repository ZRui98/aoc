import re
from copy import deepcopy
file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

workflows = {}

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

def recurse(ranges={'x':[1, 4000], 'm':[1, 4000], 'a':[1, 4000], 's':[1, 4000]}, workflow='in'):
    if workflow not in workflows:
        if workflow == 'A':
            # print(ranges, workflow, (ranges['x'][1] - ranges['x'][0] + 1) * (ranges['m'][1] - ranges['m'][0] + 1) * (ranges['a'][1] - ranges['a'][0] + 1) * (ranges['s'][1] - ranges['s'][0] + 1))
            return (ranges['x'][1] - ranges['x'][0] + 1) * (ranges['m'][1] - ranges['m'][0] + 1) * (ranges['a'][1] - ranges['a'][0] + 1) * (ranges['s'][1] - ranges['s'][0] + 1)
        else:
            return 0
    ans = 0
    newranges = deepcopy(ranges)
    for rule in workflows[workflow]:
        if '<' not in rule[0] and '>' not in rule[0]:
            ans += recurse(newranges, rule[1])
        else:
            var, mid = re.split('<|>', rule[0])
            mid = int(mid)
            if newranges[var][0] < mid < newranges[var][1]:
                if '<' in rule[0]:
                    tmp = newranges[var][1]
                    newranges[var][1] = mid - 1
                    ans += recurse(ranges=newranges, workflow=rule[1])
                    newranges[var] = [mid, tmp]
                else:
                    tmp = newranges[var][0]
                    newranges[var][0] = mid + 1
                    ans += recurse(ranges=newranges, workflow=rule[1])
                    newranges[var] = [tmp, mid]
    return ans
    
print(recurse())