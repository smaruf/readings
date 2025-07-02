import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class ExtendedCrossPatternsNoCenterEquality {

    public static List<int[]> detectExtendedCrossPatternsNoCenterEquality(int[][] matrix) {
        List<int[]> crossPositions = new ArrayList<>();
        int n = matrix.length;

        // Precompute row values and column values for efficiency
        int[] rowUniformValue = new int[n];
        int[] colUniformValue = new int[n];
        boolean[] isRowUniform = new boolean[n];
        boolean[] isColUniform = new boolean[n];

        // Check uniformity for each row
        for (int i = 0; i < n; i++) {
            int val = matrix[i][0];
            boolean uniform = true;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] != val) {
                    uniform = false;
                    break;
                }
            }
            isRowUniform[i] = uniform;
            rowUniformValue[i] = val;
        }

        // Check uniformity for each column
        for (int j = 0; j < n; j++) {
            int val = matrix[0][j];
            boolean uniform = true;
            for (int i = 1; i < n; i++) {
                if (matrix[i][j] != val) {
                    uniform = false;
                    break;
                }
            }
            isColUniform[j] = uniform;
            colUniformValue[j] = val;
        }

        // Now, for every position, if its row and column are uniform, it's a cross pattern
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isRowUniform[i] && isColUniform[j]) {
                    crossPositions.add(new int[]{i, j});
                }
            }
        }

        return crossPositions;
    }

    public static void main(String[] args) {
        // Test 1: All uniform rows and columns
        int[][] matrix1 = {
            {5, 5, 5},
            {5, 5, 5},
            {5, 5, 5}
        };
        runTest(matrix1, "All uniform rows and columns");

        // Test 2: No uniform rows or columns
        int[][] matrix2 = {
            {1, 2},
            {3, 4}
        };
        runTest(matrix2, "No uniform rows or columns");

        // Test 3: Some uniform rows, no uniform columns
        int[][] matrix3 = {
            {7, 7, 7},
            {1, 2, 3},
            {4, 4, 4}
        };
        runTest(matrix3, "Some uniform rows, no uniform columns");

        // Test 4: Only first column uniform
        int[][] matrix4 = {
            {8, 2, 3},
            {8, 5, 6},
            {8, 9, 1}
        };
        runTest(matrix4, "Only first column uniform");

        // Test 5: Mixed uniform row and column
        int[][] matrix5 = {
            {1, 2, 3},
            {4, 4, 4},
            {7, 8, 9}
        };
        runTest(matrix5, "Mixed uniform row and column");
    }

    private static void runTest(int[][] matrix, String description) {
        System.out.println("Test: " + description);
        List<int[]> result = detectExtendedCrossPatternsNoCenterEquality(matrix);
        System.out.println("Cross positions:");
        for (int[] pos : result) {
            System.out.println(Arrays.toString(pos));
        }
        System.out.println("-----");
    }
}
