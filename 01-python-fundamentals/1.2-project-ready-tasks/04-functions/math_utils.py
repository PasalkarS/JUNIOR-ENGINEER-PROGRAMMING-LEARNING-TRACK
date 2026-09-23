# Math Utility Library
# Collection of reusable pure functions with type hints and docstrings.

def calculate_mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(values) / len(values)

def calculate_median(values: list[float]) -> float:
    """Return the median of a list of numbers."""
    if not values:
        raise ValueError("Cannot calculate median of an empty list.")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0

def clamp(val: float, min_val: float, max_val: float) -> float:
    """Clamp a value to be within [min_val, max_val]."""
    return max(min_val, min(val, max_val))

if __name__ == "__main__":
    data = [12.0, 4.0, 5.0, 9.0, 20.0]
    print("Data:", data)
    print("Mean:", calculate_mean(data))
    print("Median:", calculate_median(data))
    print("Clamp 25 into [0, 10]:", clamp(25, 0, 10))
