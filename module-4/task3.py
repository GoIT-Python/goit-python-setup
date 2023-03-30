def format_ingredients(items):
    result = ""
    if len(items) > 0:
        if len(items) == 1:
            result += f"{items[0]}"
        elif len(items) == 2:
            result = f"{items[0]} and {items[-1]}"
        else:
            memo = items[0:-1]
            for i in memo:
                if not i == memo[-1]:
                    result += f"{i}, " ""
                else:
                    result += f"{i} and " ""

            result += items[-1]

    return result


print(format_ingredients(["2 eggs"]))

# Ожидалось, что format_ingredients(['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']) == '2 eggs, 1 liter sugar, 1 tsp salt and vinegar'
