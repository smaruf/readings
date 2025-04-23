def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    # Initialize the first two steps
    prev, curr = 1, 2

    for i in range(3, n + 1):
        # Update steps iteratively
        prev, curr = curr, prev + curr

    return curr

# Example usage
if __name__ == "__main__":
    n = 5  # Number of steps
    print(f"Number of ways to climb {n} steps: {climb_stairs(n)}")
