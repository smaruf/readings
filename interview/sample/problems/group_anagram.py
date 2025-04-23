from collections import defaultdict

def groupAnagrams(strs):
    # Use a dictionary to map sorted string to the list of anagrams
    anagrams = defaultdict(list)

    for s in strs:
        # Sort the string and use it as the key
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)

    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
