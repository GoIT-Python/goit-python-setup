from random import randint, choice

SIZE_W = randint(5, 12)
SIZE_H = randint(5, 12)


def check_state(char_hero, char_x, char_y, exit_x, exit_y, enemy_x, enemy_y):
    win = char_x == exit_x and char_y == exit_y
    fail_condition = char_x == enemy_x and char_y == enemy_y

    if win:
        char_hero = "W"
        print(f"Game over! You won in {step_count} step!")
    elif fail_condition:
        char_hero = "F"
        print(f"You failed in {step_count} steps")

    return char_hero, win or fail_condition


def draw_map(
    char_x,
    char_y,
    char_hero,
    exit_x,
    exit_y,
    exit_sign,
    enemy_x,
    enemy_y,
    char_enemy,
    size_w=SIZE_W,
    size_h=SIZE_H,
):
    world_map = ""

    for j in range(size_h):
        row = " | "

        for i in range(size_w):
            if char_x == i and char_y == j:
                row += f"{char_hero}| "
            elif enemy_x == i and enemy_y == j:
                row += f"{char_enemy}| "
            elif exit_x == i and exit_y == j:
                row += f"{exit_sign}| "
            else:
                row += " | "

        world_map += f"{row}\n"

    return world_map


def move(direction, x, y, size_w=SIZE_W, size_h=SIZE_H):
    if direction == "u" and y > 0:
        y -= 1
    elif direction == "d" and y < size_h - 1:
        y += 1
    elif direction == "l" and x > 0:
        x -= 1
    elif direction == "r" and x < size_w - 1:
        x += 1

    return x, y


char_x = randint(0, SIZE_W - 1)
char_y = randint(0, SIZE_H - 1)
char_hero = "H"

enemy_x = randint(0, SIZE_W - 1)
enemy_y = randint(0, SIZE_H - 1)
char_enemy = "E"

exit_x = randint(0, SIZE_W - 1)
exit_y = randint(0, SIZE_H - 1)
exit_sign = "S"


step_count = 0

while True:
    char_hero, game_over = check_state(
        char_hero, char_x, char_y, exit_x, exit_y, enemy_x, enemy_y
    )

    print(
        draw_map(
            char_x,
            char_y,
            char_hero,
            exit_x,
            exit_y,
            exit_sign,
            enemy_x,
            enemy_y,
            char_enemy,
        )
    )

    if game_over:
        break

    direction = input("Enter direction (u / d / l / r): ")
    char_x, char_y = move(direction, char_x, char_y)

    enemy_direction = choice("udlr")
    enemy_x, enemy_y = move(enemy_direction, enemy_x, enemy_y)

    step_count += 1
