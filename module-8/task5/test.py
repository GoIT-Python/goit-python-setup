import random

fruits = ["apple", "banana", "orange"]
print(fruits)
random.shuffle(fruits)
print(fruits)  # ['banana', 'orange', 'apple']

print(random.sample(fruits, k=2))  # ['banana', 'orange']
