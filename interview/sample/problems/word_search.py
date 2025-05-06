def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(row, col, index):
        # If the full word is matched
        if index == len(word):
            return True
        
        # Check boundaries and if the cell matches the current character
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
            return False
        
        # Mark the cell as visited (use a placeholder)
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explore all four directions
        found = (
            dfs(row + 1, col, index + 1) or
            dfs(row - 1, col, index + 1) or
            dfs(row, col + 1, index + 1) or
            dfs(row, col - 1, index + 1)
        )
        
        # Backtrack by restoring the cell
        board[row][col] = temp
        return found

    # Start DFS from each cell
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    
    return False

# Example Usage
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
print(exist(board, word))  # Output: True
