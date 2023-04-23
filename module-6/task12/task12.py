import base64

data = ["andry:uyro18890D", "steve:oppjM13LL9e"]


def encode_data_to_base64(data):
    list = []
    for item in data:
        data_bytes = item.encode("utf-8")
        base64_bytes = base64.b64encode(data_bytes)
        base64_data = base64_bytes.decode("utf-8")
        list.append(base64_data)

    return list


encode_data_to_base64(data)

# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
