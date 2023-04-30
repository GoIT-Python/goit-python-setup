import re

regex = "[//.|//!|//?]"

# text = "alert. boss! oh"
text = "hello world! awesome? yes"

res = [x for x in re.split(regex, text) if x != ""]
print(res)
