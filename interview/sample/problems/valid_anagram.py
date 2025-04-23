from collections import Counter

def isAnagram(s, t):
    # Compare the frequency of characters in both strings
    return Counter(s) == Counter(t)

# Example usage
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True

s = "rat"
t = "car"
print(isAnagram(s, t))  # Output: False
