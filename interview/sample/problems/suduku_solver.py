def solveSudoku(board):
    def isValid(board, row, col, num):
        # Check the row
        for i in range(9):
            if board[row][i] == num:
                return False
        
        # Check the column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check the 3x3 subgrid
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False
        
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # Empty cell
                    for num in map(str, range(1, 10)):
                        if isValid(board, row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = '.'  # Backtrack
                    return False  # Trigger backtracking
        return True  # Solved

    backtrack()

# Example Usage
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

solveSudoku(sudoku_board)
for row in sudoku_board:
    print(row)
