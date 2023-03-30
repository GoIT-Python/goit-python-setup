points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0

    else:
        result = 0

    count = 0

    while True:
        memo = (coordinates[count], coordinates[count + 1])

        if memo[0] > memo[1]:
            a = memo[0]
            b = memo[1]
            a, b = b, a
            memo = (a, b)

        if memo in points:
            result += points[memo]

        if count >= len(coordinates) - 2:
            break

        count += 1

    return float(result)


print(calculate_distance([0, 1, 3, 2, 0]))
