def longestConsecutive(nums):
    # Convert the list to a set for O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # Output: 4 (The sequence is [1, 2, 3, 4])
