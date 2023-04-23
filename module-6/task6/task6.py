path = "task6.txt"
search_id = "60b90c3b13067a15887e1ae"


def get_recipe(path, search_id):
    list = []
    recipe = {}
    with open(path, "r") as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            list.append(line.strip().split(","))
    for item in list:
        if search_id in item:
            recipe.update({"id": item[0], "name": item[1], "ingredients": item[2:]})

    if not recipe:
        return None
    return recipe


get_recipe(path, search_id)

# {
#     "id": "60b90c3b13067a15887e1ae4",
#     "name": "Watermelon Cucumber Salad",
#     "ingredients": [
#         "1 large seedless watermelon",
#         "12 leaves fresh mint",
#         "1 cup crumbled feta cheese",
#     ],
# }
