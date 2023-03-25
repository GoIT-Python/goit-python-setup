base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1
    return float(base_rate + price_per_km * path)


trip_price(4.3)

# Вызов функции вернул неправильный результат: trip_price_test(4.3). Ожидалось значение: 83.0. Функция вернула 19.30232558139535
