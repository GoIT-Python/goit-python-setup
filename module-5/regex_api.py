import re

# regexp = r"^[0-2][0-5]"
regexp = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"

ips = [
    "0.0.0.0",
    "0000",
    "128.13.10.41",
    "123.45.84",
    "123,123,123,123",
    "1234567890",
    "245.520.18.17",
]

for ip in ips:
    result = re.search(regexp, ip)

    if result is None:
        print(f"Negative result: {ip}")
    else:
        print(f"Positive result: {result.group()}")
