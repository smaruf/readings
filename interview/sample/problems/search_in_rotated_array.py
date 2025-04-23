def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the middle element is the target
        if nums[mid] == target:
            return mid

        # Determine which part of the array is sorted
        if nums[left] <= nums[mid]:  # Left part is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target is in the left part
            else:
                left = mid + 1   # Target is in the right part
        else:  # Right part is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target is in the right part
            else:
                right = mid - 1  # Target is in the left part

    return -1  # Target not found

# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))  # Output: 4

target = 3
print(search(nums, target))  # Output: -1
