def permute(nums):
    result = [[]]  # Start with an empty permutation

    for num in nums:
        new_result = []
        for perm in result:
            # Insert the current number at every position in the current permutation
            for i in range(len(perm) + 1):
                new_result.append(perm[:i] + [num] + perm[i:])
        result = new_result

    return result

# Example Usage
nums = [1, 2, 3]
print(permute(nums))
# Output: [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
