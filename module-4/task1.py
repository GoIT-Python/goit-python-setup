def amount_payment(payment):
    due_sum = 0
    for sum in payment:
        if sum > 0:
            due_sum += sum
    return due_sum


print(amount_payment([2, 4, 7, -5]))
