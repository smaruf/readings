def isPalindrome(s):
    # Use two pointers
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the characters, ignoring case
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Example usage
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True

s = "race a car"
print(isPalindrome(s))  # Output: False
