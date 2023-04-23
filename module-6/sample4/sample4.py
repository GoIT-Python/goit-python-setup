output = "sample4.txt"


def encrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)
    for idx, byte in enumerate(b_obj_array):
        n = byte + key
        if n > 255:
            n -= 255
        b_obj_array[idx] = n
    return bytes(b_obj_array)


def decrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)
    for idx, byte in enumerate(b_obj_array):
        n = byte - key
        if n < 0:
            n += 255
        b_obj_array[idx] = n
    return bytes(b_obj_array)


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    pwd_key = int(input("Enter key: "))
    pwd_bytes = pwd.encode()
    encrypted_pwd = encrypt(pwd_bytes, pwd_key)

with open(output, "wb") as file:
    file.write(encrypted_pwd)

with open(output, "rb") as file:
    encrypted_pwd = file.read()
    pwd_key = int(input("Enter key: "))
    password = decrypt(encrypted_pwd, pwd_key)
    print(password)
