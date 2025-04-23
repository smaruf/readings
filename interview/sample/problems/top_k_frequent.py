from collections import Counter
import heapq

def topKFrequent(nums, k):
    # Count the frequency of each element
    freq_map = Counter(nums)
    
    # Use a heap to get the k most frequent elements
    return heapq.nlargest(k, freq_map.keys(), key=freq_map.get)

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]
