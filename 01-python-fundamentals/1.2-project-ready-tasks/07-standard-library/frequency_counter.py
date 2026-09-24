from collections import Counter
import re

text = input("Enter some text: ")

words = re.findall(r"\w+", text.lower())

frequency = Counter(words)

print("Word frequency:")

for word, count in frequency.items():
    print(word, ":", count)
