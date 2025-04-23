from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    # Count the frequency of characters in t
    t_count = Counter(t)
    required = len(t_count)

    # Sliding window pointers
    left, right = 0, 0
    formed = 0
    window_counts = {}

    # Result variables to track the minimum window
    min_len = float("inf")
    min_window = (0, 0)

    while right < len(s):
        # Add the character at the right pointer to the window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if the current character satisfies the condition for t
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Try and contract the window till it ceases to be 'desirable'
        while left <= right and formed == required:
            char = s[left]

            # Update the minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            # Remove the character at the left pointer from the window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            left += 1  # Move the left pointer

        # Expand the window by moving the right pointer
        right += 1

    # Return the minimum window or an empty string if no window is found
    return "" if min_len == float("inf") else s[min_window[0]:min_window[1] + 1]

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output: "BANC"
