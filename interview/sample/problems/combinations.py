def combine(n, k):
    result = []
    
    def backtrack(start, combination):
        # Base case: if the combination size equals k, add it to the result
        if len(combination) == k:
            result.append(combination[:])  # Make a copy of the combination
            return
        
        for i in range(start, n + 1):
            # Include the current number in the combination
            combination.append(i)
            backtrack(i + 1, combination)  # Recurse for the next number
            # Backtrack: remove the current number
            combination.pop()
    
    backtrack(1, [])
    return result

# Example usage
n = 4
k = 2
print(combine(n, k))  
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
