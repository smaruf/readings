import java.util.ArrayList;
import java.util.List;

public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> results = new ArrayList<>();
        char[][] board = new char[n][n];
        
        // Initialize the board with '.'
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }
        
        backtrack(0, board, results, n);
        return results;
    }
    
    private void backtrack(int row, char[][] board, List<List<String>> results, int n) {
        if (row == n) {
            // Convert the board to a list of strings and add it to results
            List<String> solution = new ArrayList<>();
            for (char[] chars : board) {
                solution.add(new String(chars));
            }
            results.add(solution);
            return;
        }
        
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col, n)) {
                // Place the queen
                board[row][col] = 'Q';
                backtrack(row + 1, board, results, n);
                // Backtrack: Remove the queen
                board[row][col] = '.';
            }
        }
    }
    
    private boolean isValid(char[][] board, int row, int col, int n) {
        // Check the column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }
        
        // Check the main diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        // Check the anti-diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        return true;
    }

    public static void main(String[] args) {
        NQueens nQueens = new NQueens();
        List<List<String>> solutions = nQueens.solveNQueens(4);
        
        for (List<String> solution : solutions) {
            for (String row : solution) {
                System.out.println(row);
            }
            System.out.println();
        }
    }
}
