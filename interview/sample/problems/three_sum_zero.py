def threeSum(nums):
    nums.sort()  # Sort the array to simplify finding triplets
    result = []

    for i in range(len(nums)):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers to find the other two numbers
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Increase the sum by moving the left pointer
            else:
                right -= 1  # Decrease the sum by moving the right pointer

    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
