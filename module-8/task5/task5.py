import random

quantity = 2
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}


def get_random_winners(quantity, participants):
    if not quantity < len(participants):
        return []
    list = []
    for key in participants.keys():
        list.append(key)
    random.shuffle(list)
    print(random.sample(list, k=quantity))
    return random.sample(list, k=quantity)


get_random_winners(quantity, participants)

# def get_random_winners(quantity, participants):
#     if  quantity > len(participants):
#         return []
#     list = []
#     for key in participants.keys():
#         list.append(key)
#     random.shuffle(list)
#     return random.sample(list, k=quantity)
