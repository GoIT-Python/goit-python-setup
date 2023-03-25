# |   |   |   |   | O |
# |   |   |   |   |   |
# |   |   |   |   |   |
# |   |   |   |   |   |
# |   |   |   |   |   |
# |   |   |   | X |   |

from random import randint

SIZE_W = 5
SIZE_H = 5


char_x = randint(0, SIZE_W - 1)
char_y = randint(0, SIZE_H - 1)

char_hero = "X"

exit_x = randint(0, SIZE_W - 1)
exit_y = randint(0, SIZE_H - 1)

step_count = 0

while True:
    world_map = ""

    win = char_x == exit_x and char_y == exit_y

    if win:
        char_hero = "W"

    for j in range(SIZE_H):
        row = " | "

        for i in range(SIZE_W):
            if char_x == i and char_y == j:
                row += f"{char_hero}| "
            elif exit_x == i and exit_y == j:
                row += "E| "
            else:
                row += " | "

        world_map += f"{row}\n"

    print(world_map)

    if win:
        print(f"You won in {step_count} step!")
        break

    direction = input("Enter direction (u / d / l / r): ")

    if direction == "u" and char_y > 0:
        char_y -= 1
    elif direction == "d" and char_y < SIZE_H - 1:
        char_y += 1
    elif direction == "l" and char_x > 0:
        char_x -= 1
    elif direction == "r" and char_x < SIZE_W - 1:
        char_x += 1

    step_count += 1
