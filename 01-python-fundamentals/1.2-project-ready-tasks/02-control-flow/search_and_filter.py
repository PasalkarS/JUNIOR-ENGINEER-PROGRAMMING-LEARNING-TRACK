# Searching and Filtering
# Demonstrates loop control with break and continue.

scores = [45, 78, 92, 33, 85, 12, 64, 99, 58]
passing_threshold = 60
target_top_score = 90

print("Passing Scores:")
for score in scores:
    if score < passing_threshold:
        continue  # Skip failing scores
    print(f" - {score} (PASSED)")

print("\nFirst Honor Student Search:")
for score in scores:
    if score >= target_top_score:
        print(f"Found top score: {score}! Stopping search.")
        break
