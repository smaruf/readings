def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    # Step 1: Compute prefix product
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Step 2: Compute suffix product and multiply with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

# Example usage
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
