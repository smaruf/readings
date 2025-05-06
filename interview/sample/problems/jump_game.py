def canJump(nums):
    maxReach = 0
    for i in range(len(nums)):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
    return True

# Example Usage
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
print(canJump(nums1))  # Output: True
print(canJump(nums2))  # Output: False
