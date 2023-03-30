def game(terra, power):
    count = 0

    while count < len(terra):
        for i in terra[count]:
            if not i > power:
                power += i
            else:
                break
        count += 1

    return power


print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))
