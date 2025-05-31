import java.util.ArrayList;
import java.util.List;

public class NxNCrossDetector {

    public static List<int[]> detectCrosses(int[][] matrix) {
        List<int[]> crosses = new ArrayList<>();
        int n = matrix.length;

        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (matrix[i - 1][j] == matrix[i + 1][j] &&
                    matrix[i][j - 1] == matrix[i][j + 1]) {
                    crosses.add(new int[]{i, j});
                }
            }
        }

        return crosses;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3, 2, 1},
            {4, 5, 6, 5, 4},
            {7, 8, 9, 8, 7},
            {4, 5, 6, 5, 4},
            {1, 2, 3, 2, 1}
        };

        List<int[]> crosses = detectCrosses(matrix);

        System.out.println("Cross centers found at:");
        for (int[] pos : crosses) {
            System.out.println("(" + pos[0] + ", " + pos[1] + ")");
        }
    }
}
