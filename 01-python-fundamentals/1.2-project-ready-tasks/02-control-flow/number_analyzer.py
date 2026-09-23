# Number Analyzer
# Analyzes a list of numbers: positive/negative, odd/even, zero.

numbers = [12, -7, 0, 45, -2, 18, 0, -9]

positives = 0
negatives = 0
zeros = 0
evens = 0
odds = 0

for num in numbers:
    # Sign analysis
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeros += 1

    # Parity analysis (only for non-zero numbers)
    if num != 0:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1

print(f"Total numbers: {len(numbers)}")
print(f"Positives: {positives}, Negatives: {negatives}, Zeros: {zeros}")
print(f"Evens: {evens}, Odds: {odds}")
