def combine(n, k):
    result = [[]]  # Start with an empty combination

    for num in range(1, n + 1):
        new_result = []
        for comb in result:
            # Only add the number if it doesn't exceed the required size
            if len(comb) < k:
                new_result.append(comb + [num])
        result += new_result

    return [comb for comb in result if len(comb) == k]

# Example Usage
n = 4
k = 2
print(combine(n, k))
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
