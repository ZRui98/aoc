file = open('input.txt', 'r')
lines = [line.rstrip('\n') for line in file]

N = len(lines)
total = 0
current = 0
operation = ''
for i in range(len(lines[0])):
    digits = ''
    for j in range(N-1):
        if lines[j][i] == ' ':
            continue
        digits += lines[j][i]
    if not digits:
        total += current
        current = 0
        continue
    number = int(digits)
    # new question
    if lines[-1][i] != ' ':
        operation = lines[-1][i]
        if operation == '+':
            current = 0
        if operation == '*':
            current = 1
    if operation == '+':
        current += number
    if operation == '*':
        current *= number

print(total + current)