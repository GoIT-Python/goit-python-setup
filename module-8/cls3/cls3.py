import random

# number=random.randint(0,100)
number=random.random()
# print(number)

mt_list=list(range(0,10))
print(mt_list)
random.shuffle(mt_list)
print(mt_list)

print(random.choice(mt_list))
print(random.choices(mt_list,k=2))
print(random.sample(mt_list, k=2))

