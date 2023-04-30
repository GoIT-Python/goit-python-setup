import re

regex = r"[^.!?]+"

text = "alert. boss! oh"

res = re.findall(regex, text)

print(res)
