from random import randint, choice

SIZE_W = randint(5, 12)
SIZE_H = randint(5, 12)

ENEMIES_NUMBER = 5


def check_state(objects):
    for obj in objects:
        if obj["type"] == "hero":
            hero = obj

        elif obj["type"] == "portal":
            portal = obj

        elif obj["type"] == "enemy":
            fail_condition = hero["x"] == obj["x"] and hero["y"] == obj["y"]

            if fail_condition:
                hero["sign"] = "F"
                print(f"You failed in {step_count} steps")
                break

    win = hero["x"] == portal["x"] and hero["y"] == portal["y"]

    if win:
        hero["sign"] = "W"
        print(f"Game over! You won in {step_count} step!")

    return win or fail_condition


def generate_enemies(number):
    enemies = []

    for _ in range(number):
        enemy = {
            "x": randint(0, SIZE_W - 1),
            "y": randint(0, SIZE_H - 1),
            "sign": "E",
            "type": "enemy",
        }

        enemies.append(enemy)

    return enemies


def draw_map(
    objects,
    size_w=SIZE_W,
    size_h=SIZE_H,
):
    world_map = []

    for j in range(size_h):
        row = []

        for i in range(size_w):
            row.append(" ")

        world_map.append(row)

    # for obj in objects:
    #     world_map[obj["y"]][obj["x"]] = obj["sign"]

    return world_map


def move(direction, obj, size_w=SIZE_W, size_h=SIZE_H):
    if direction == "u" and obj["y"] > 0:
        obj["y"] -= 1
    elif direction == "d" and obj["y"] < size_h - 1:
        obj["y"] += 1
    elif direction == "l" and obj["x"] > 0:
        obj["x"] -= 1
    elif direction == "r" and obj["x"] < size_w - 1:
        obj["x"] += 1


def print_map(world_map):
    for row in world_map:
        print(f'|{"|".join(row)}|')


hero = {
    "x": randint(0, SIZE_W - 1),
    "y": randint(0, SIZE_H - 1),
    "sign": "H",
    "type": "hero",
}


portal = {
    "x": randint(0, SIZE_W - 1),
    "y": randint(0, SIZE_H - 1),
    "sign": "S",
    "type": "portal",
}

enemies = generate_enemies(ENEMIES_NUMBER)


objects = [hero, portal] + enemies


step_count = 0

while True:
    game_over = check_state(objects)
    world_map = draw_map(object)
    print(world_map)

    if game_over:
        break

    for obj in object:
        direction = ""

        if obj["type"] == "hero":
            direction = input("Enter direction (u / d / l / r): ")

        elif obj["type"] == "enemy":
            direction = choice("udlr")

        move(direction, obj)

    step_count += 1
