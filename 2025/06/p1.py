file = open('input.txt', 'r')
lines = [line.rstrip().split() for line in file]
questions = list(zip(*lines))

total = 0

for question in questions:
    operation = question[-1]
    ans = 0
    if operation == '+':
        for i in range(len(question) - 1):
            ans += int(question[i])
            
    elif operation == '*':
        ans = 1
        for i in range(len(question) - 1):
            ans *= int(question[i])
    total += ans

print(total)