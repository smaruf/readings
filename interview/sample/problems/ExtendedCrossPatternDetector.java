import java.util.ArrayList;
import java.util.List;

public class ExtendedCrossPatternDetector {

    /**
     * Detects extended cross patterns in the given matrix.
     * A cross pattern exists at position (i, j) if:
     * - All elements in row i are equal to matrix[i][j]
     * - All elements in column j are equal to matrix[i][j]
     *
     * @param matrix The input n x n matrix.
     * @return A list of positions where cross patterns are detected.
     */
    public static List<int[]> detectExtendedCrossPatterns(int[][] matrix) {
        List<int[]> crossPositions = new ArrayList<>();
        int n = matrix.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int centerValue = matrix[i][j];
                boolean isCross = true;

                // Check all elements in row i
                for (int col = 0; col < n; col++) {
                    if (matrix[i][col] != centerValue) {
                        isCross = false;
                        break;
                    }
                }

                // Check all elements in column j
                if (isCross) {
                    for (int row = 0; row < n; row++) {
                        if (matrix[row][j] != centerValue) {
                            isCross = false;
                            break;
                        }
                    }
                }

                if (isCross) {
                    crossPositions.add(new int[]{i, j});
                }
            }
        }

        return crossPositions;
    }

    public static void main(String[] args) {
        // Example matrix
        int[][] matrix = {
            {1, 2, 3, 2, 1},
            {4, 5, 6, 5, 4},
            {7, 8, 9, 8, 7},
            {4, 5, 6, 5, 4},
            {1, 2, 3, 2, 1}
        };

        List<int[]> crossPositions = detectExtendedCrossPatterns(matrix);

        System.out.println("Extended cross patterns found at positions:");
        for (int[] pos : crossPositions) {
            System.out.println("Row: " + pos[0] + ", Column: " + pos[1]);
        }
    }
}
