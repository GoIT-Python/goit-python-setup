from collections import defaultdict


words = ["apple", "zoo", "lion", "lama", "bear", "bet", "wolf", "appendix"]
grouped_words = defaultdict(list)

print(grouped_words)

for word in words:
    char = word[0]
    grouped_words[char].append(word)
