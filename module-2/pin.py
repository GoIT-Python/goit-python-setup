initail_pin = "1234"
access_granted = False

count = 0
max_attempts = 3

while count < max_attempts:
    print(f"You have {max_attempts-count} tries left")

    user_pin = input("Enter PIN: ")

    if len(user_pin) == 4 or len(user_pin) == 6:
        if initail_pin == user_pin:
            access_granted = True
            print("Access granted!")
            amount = input("Enter amount: ")

            if amount > 0:
                print(f"Take your amount: {amount}")
                break
            else:
                print("Amount should be positive")

        else:
            print("Wrong PIN, try again")

    else:
        print("PIN should be 4 or 6 digits")

    count += 1

    if count == max_attempts and not access_granted:
        print("Reach maximum attempts")

# for i in range(3):
#     user_pin = input("Enter PIN: ")

#     if len(user_pin) == 4 or len(user_pin) == 6:
#         if initail_pin == user_pin:
#             print("Access granted!")
#             break
#         else:
#             print("Wrong PIN, try again")

#     else:
#         print("PIN should be 4 or 6 digits")

# print("Reach maximum attempts")
