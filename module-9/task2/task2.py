DEFAULT_DISCOUNT = 0.05

price = 100
# customer = {"name": "Dima"}
customer = {"name": "Boris", "discount": 0.15}


def get_discount_price_customer(price, customer):
    discount = customer.get("discount", DEFAULT_DISCOUNT)
    price *= 1 - discount
    print(price)
    return price


get_discount_price_customer(price, customer)

# GLOBAL_SCOPE_VAR = 1


# def func():
#     enclosed_scope_var = 2

#     def inner():
#         inner_var = 3
