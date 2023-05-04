from decimal import Decimal, getcontext

# print(0.1+0.2)

# print(0.1+0.2==0.3)

getcontext().prec = 4
result=Decimal(1)/Decimal(7)  # Decimal('0.142857')
print(result)

getcontext().prec = 5
result=Decimal(1)/Decimal(7)  # Decimal('0.142857')
print(result)

# print(float(Decimal(0.1)))



