def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If the middle element is greater than the rightmost element
        # then the minimum is in the right part
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum is in the left part (including mid)
            right = mid

    return nums[left]

# Example usage
nums = [3, 4, 5, 1, 2]
print(findMin(nums))  # Output: 1

nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # Output: 0

nums = [11, 13, 15, 17]
print(findMin(nums))  # Output: 11
