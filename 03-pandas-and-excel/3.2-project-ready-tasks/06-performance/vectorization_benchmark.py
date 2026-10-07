import pandas as pd
import time

numbers = list(range(1, 1000001))

df = pd.DataFrame({
    "Number": numbers
})

# Slow approach
start_time = time.time()

results = []

for number in df["Number"]:
    results.append(number * 2)

loop_time = time.time() - start_time

# Vectorized approach
start_time = time.time()

df["Vectorized_Result"] = df["Number"] * 2

vectorized_time = time.time() - start_time

print("Loop time:", loop_time)
print("Vectorized time:", vectorized_time)

print("\nFirst 5 results:")
print(df.head())

print("\nVectorized operation is generally faster because")
print("Pandas performs the calculation efficiently on the whole column.")
