def cost_delivery(quantity, *_, discount=0):
    first_unit = 5
    rest_unit = 2

    if quantity > 1:
        return (
            first_unit
            + (quantity - 1) * rest_unit
            - (first_unit + (quantity - 1) * rest_unit) * discount
        )
    elif quantity == 1:
        return quantity * first_unit - (quantity * first_unit) * discount


print(cost_delivery(2, 1, 2, 3))

print(cost_delivery(3, 3))

print(cost_delivery(1))

print(cost_delivery(2, 1, 2, 3, discount=0.5))
