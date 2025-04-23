import heapq

def kthSmallest(matrix, k):
    n = len(matrix)
    # Min-heap to store (value, row, col)
    min_heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(min_heap)
    
    # Extract k elements from the heap
    for _ in range(k - 1):
        val, row, col = heapq.heappop(min_heap)
        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    
    return heapq.heappop(min_heap)[0]

# Example usage
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(kthSmallest(matrix, k))  # Output: 13
