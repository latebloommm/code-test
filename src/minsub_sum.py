def sum_to_n(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) // 2
