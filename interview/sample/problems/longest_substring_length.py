def lengthOfLongestSubstring(s):
    # Initialize a set to store characters and two pointers
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If character is already in the set, remove characters from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set
        char_set.add(s[right])
        # Calculate the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3 (The substring is "abc")
