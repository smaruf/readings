public class MatrixRotationNonSquare {

    public static int[][] rotate90Clockwise(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] rotated = new int[n][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][m - 1 - i] = matrix[i][j];
            }
        }
        return rotated;
    }

    public static int[][] rotate90CounterClockwise(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] rotated = new int[n][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated[n - 1 - j][i] = matrix[i][j];
            }
        }
        return rotated;
    }

    public static int[][] rotate180(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] rotated = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated[m - 1 - i][n - 1 - j] = matrix[i][j];
            }
        }
        return rotated;
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row)
                System.out.print(val + " ");
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        System.out.println("\n90° Clockwise:");
        printMatrix(rotate90Clockwise(matrix));

        System.out.println("\n90° Counter-Clockwise:");
        printMatrix(rotate90CounterClockwise(matrix));

        System.out.println("\n180° Rotation:");
        printMatrix(rotate180(matrix));
    }
}
