file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]

def find_max_power(bank):
    for i in reversed(range(10)):
        f = bank.find(str(i))
        if f == -1:
            continue
        for j in reversed(range(10)):
            s = bank.find(str(j), f + 1)
            if s != -1:
                return i * 10 + j
    return 0

ans = 0

for bank in lines:
    power = find_max_power(bank)
    print(bank, power)
    ans += power

print(ans)