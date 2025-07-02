public class MatrixRotation180Degrees {

    public static void rotate180(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < m; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - i][m - 1 - j];
                matrix[n - 1 - i][m - 1 - j] = temp;
            }
        }

        // If n is odd, reverse the middle row
        if (n % 2 != 0) {
            int mid = n / 2;
            for (int j = 0; j < m / 2; j++) {
                int temp = matrix[mid][j];
                matrix[mid][j] = matrix[mid][m - 1 - j];
                matrix[mid][m - 1 - j] = temp;
            }
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        rotate180(matrix);

        System.out.println("Rotated Matrix (180 degrees):");
        printMatrix(matrix);
    }
}
