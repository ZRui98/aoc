file = open('input.txt', 'r')
lines = [line.rstrip() for line in file]
max_dice = {'red': 12, 'green': 13, 'blue': 14}

def valid_game(dice):
    print(dice)
    for d in dice:
        if int(d[0]) > max_dice[d[1]]:
            return False
    return True

ans = 0
for game in lines:
    l = game.split(': ')
    id = int(l[0].split(' ')[-1])
    rounds = l[1].split('; ')
    game_dice = []
    for round in rounds:
        round_dice = round.split(', ')
        for d in round_dice:
            game_dice.append(d.split(' '))
    # pt1
    # if valid_game(game_dice):
    #     ans += id

    state = {'red': 0, 'green': 0, 'blue': 0}
    for d in game_dice:
        if int(d[0]) > state[d[1]]:
            state[d[1]] = int(d[0])
    cnt = list(state.values())
    power = cnt[0] * cnt[1] * cnt[2]
    print(power)
    ans += power
print(ans)