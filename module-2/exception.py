while True:
    user_input = input("Enter number: ")

    try:
        int(user_input)
    except ValueError:
        print("ValueError")
        continue
    except TypeError:
        print("TypeError")
        continue
    else:
        print("Else")
    finally:
        print("Finally")

    break
