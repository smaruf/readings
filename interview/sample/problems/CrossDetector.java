import java.util.ArrayList;
import java.util.List;

public class CrossDetector {

    public static List<int[]> detectCrosses(int[][] matrix) {
        List<int[]> crosses = new ArrayList<>();
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {

                // Top-left to bottom-right cross
                if (i + 1 < rows && j + 1 < cols) {
                    if (matrix[i][j + 1] == matrix[i + 1][j]) {
                        crosses.add(new int[]{i, j});
                    }
                }

                // Bottom-right to top-left cross
                if (i - 1 >= 0 && j - 1 >= 0) {
                    if (matrix[i][j - 1] == matrix[i - 1][j]) {
                        crosses.add(new int[]{i, j});
                    }
                }
            }
        }

        return crosses;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {2, 1},
            {1, 2}
        };

        List<int[]> result = detectCrosses(matrix);

        System.out.println("Cross positions:");
        for (int[] pos : result) {
            System.out.println("(" + pos[0] + ", " + pos[1] + ")");
        }
    }
}
