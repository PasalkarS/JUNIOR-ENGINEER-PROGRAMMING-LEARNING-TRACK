# Topic 06: Vectorization Benchmarks & Memory Downcasting
import pandas as pd
import numpy as np
import time

def benchmark_vectorization():
    n_rows = 100_000
    df = pd.DataFrame({
        "quantity": np.random.randint(1, 50, size=n_rows),
        "price": np.random.uniform(5.0, 100.0, size=n_rows),
        "status": np.random.choice(["PENDING", "COMPLETED", "FAILED"], size=n_rows)
    })

    print(f"Dataset Size: {n_rows:,} rows")
    print(f"Initial Memory Usage: {df.memory_usage(deep=True).sum() / (1024 * 1024):.2f} MB")

    # 1. Downcast to Category & float32
    df['status'] = df['status'].astype('category')
    df['price'] = df['price'].astype('float32')
    df['quantity'] = df['quantity'].astype('int16')
    print(f"Optimized Memory Usage: {df.memory_usage(deep=True).sum() / (1024 * 1024):.2f} MB")

    # 2. Benchmark Vectorized Math vs iterrows on subset
    sample_df = df.iloc[:5000].copy()

    # iterrows (slow)
    start = time.perf_counter()
    totals_loop = []
    for idx, row in sample_df.iterrows():
        totals_loop.append(row['quantity'] * row['price'])
    time_loop = time.perf_counter() - start

    # Vectorized (fast)
    start = time.perf_counter()
    sample_df['total'] = sample_df['quantity'] * sample_df['price']
    time_vec = time.perf_counter() - start

    print(f"\nBenchmark on 5,000 rows:")
    print(f" - iterrows() loop: {time_loop*1000:.2f} ms")
    print(f" - Vectorized math: {time_vec*1000:.2f} ms")
    if time_vec > 0:
        print(f" -> Vectorization is {time_loop / time_vec:.1f}x FASTER!")

if __name__ == "__main__":
    benchmark_vectorization()
