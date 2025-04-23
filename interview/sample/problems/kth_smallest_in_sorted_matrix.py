def kthSmallest(matrix, k):
    def countLessEqual(mid):
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]
    while low < high:
        mid = (low + high) // 2
        if countLessEqual(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

# Example usage
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(kthSmallest(matrix, k))  # Output: 13
