def permute(nums):
    result = []
    
    def backtrack(start):
        # Base case: if the current index reaches the end, add permutation to result
        if start == len(nums):
            result.append(nums[:])  # Make a copy of nums
            return
        
        for i in range(start, len(nums)):
            # Swap numbers to generate a new permutation
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)  # Recurse for the next index
            # Backtrack: undo the swap
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result

# Example usage
nums = [1, 2, 3]
print(permute(nums))  
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
