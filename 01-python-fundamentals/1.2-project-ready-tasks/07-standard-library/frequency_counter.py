# Frequency Counter & Statistics
# Uses collections.Counter and statistics module.

from collections import Counter
import statistics

text = "apple banana apple cherry date banana apple elderberry fig banana apple"
words = text.split()

# 1. Counter
counts = Counter(words)
print("Top 3 most frequent words:")
for word, count in counts.most_common(3):
    print(f" - {word}: {count} times")

# 2. Statistics
prices = [19.99, 24.50, 19.99, 45.00, 12.00, 19.99, 89.00]
print(f"\nPrices: {prices}")
print(f"Mean Price:   ${statistics.mean(prices):.2f}")
print(f"Median Price: ${statistics.median(prices):.2f}")
print(f"Mode Price:   ${statistics.mode(prices):.2f}")
