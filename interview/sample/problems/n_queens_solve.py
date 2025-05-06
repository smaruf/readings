def solveNQueens(n):
    def isValid(board, row, col):
        # Check the column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the main diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check the anti-diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def backtrack(row):
        if row == n:
            # Store the board configuration as a solution
            solution = ["".join(row) for row in board]
            results.append(solution)
            return
        
        for col in range(n):
            if isValid(board, row, col):
                # Place the queen
                board[row][col] = 'Q'
                backtrack(row + 1)
                # Backtrack: Remove the queen
                board[row][col] = '.'

    # Initialize the board and results
    board = [["." for _ in range(n)] for _ in range(n)]
    results = []
    backtrack(0)
    return results

# Example Usage
n = 4
solutions = solveNQueens(n)
for solution in solutions:
    print("\n".join(solution))
    print()
