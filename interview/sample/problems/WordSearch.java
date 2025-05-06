public class WordSearch {
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (board[row][col] == word.charAt(0) && dfs(board, row, col, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int row, int col, int index, String word) {
        // If the full word is matched
        if (index == word.length()) {
            return true;
        }

        // Check boundaries and if the cell matches the current character
        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length || board[row][col] != word.charAt(index)) {
            return false;
        }

        // Mark the cell as visited (use a placeholder)
        char temp = board[row][col];
        board[row][col] = '#';

        // Explore all four directions
        boolean found = dfs(board, row + 1, col, index + 1, word)
                || dfs(board, row - 1, col, index + 1, word)
                || dfs(board, row, col + 1, index + 1, word)
                || dfs(board, row, col - 1, index + 1, word);

        // Backtrack by restoring the cell
        board[row][col] = temp;
        return found;
    }

    public static void main(String[] args) {
        WordSearch ws = new WordSearch();
        char[][] board = {
            {'A', 'B', 'C', 'E'},
            {'S', 'F', 'C', 'S'},
            {'A', 'D', 'E', 'E'}
        };
        String word = "ABCCED";
        System.out.println(ws.exist(board, word));  // Output: true
    }
}
