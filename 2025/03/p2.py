import heapq

file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

N = 12

def find_max_power(bank):
    h = ''
    for c in bank:
        h+=c
        if len(h) > N:
            h = str(max([int(h[:i] + h[i+1:]) for i in range(N+1)]))
    return int(h)

ans = 0

for bank in lines:
    power = find_max_power(bank)
    print(bank, power)
    ans += power

print(ans)