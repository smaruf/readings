import bisect

def length_of_lis(nums):
    if not nums:
        return 0

    # Array to store the smallest tail of all increasing subsequences of length i + 1
    sub = []

    for num in nums:
        # Find the position to replace or extend
        i = bisect.bisect_left(sub, num)
        if i < len(sub):
            sub[i] = num  # Replace existing value to maintain the smallest possible tail
        else:
            sub.append(num)  # Extend subsequence

    return len(sub)

# Example usage
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Length of LIS: {length_of_lis(nums)}")
