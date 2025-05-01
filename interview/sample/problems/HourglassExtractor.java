import java.util.ArrayList;
import java.util.List;

public class HourglassExtractor {

    public static List<int[][]> extractHourglassBlocks(int[][] matrix, int hourglassSize) {
        int matrixSize = matrix.length;

        if (matrixSize == 0 || matrix[0].length != matrixSize) {
            throw new IllegalArgumentException("Matrix must be square (m x m)");
        }
        if (hourglassSize > matrixSize || hourglassSize % 2 == 0) {
            throw new IllegalArgumentException("Hourglass size must be odd and <= matrix size");
        }

        int center = hourglassSize / 2;
        List<int[][]> hourglasses = new ArrayList<>();

        for (int rowStart = 0; rowStart <= matrixSize - hourglassSize; rowStart++) {
            for (int colStart = 0; colStart <= matrixSize - hourglassSize; colStart++) {
                int[][] hourglass = new int[hourglassSize][hourglassSize];

                for (int localRow = 0; localRow < hourglassSize; localRow++) {
                    for (int localCol = 0; localCol < hourglassSize; localCol++) {
                        int globalRow = rowStart + localRow;
                        int globalCol = colStart + localCol;

                        if (localRow == 0 || localRow == hourglassSize - 1 || 
                            (localRow == center && localCol == center)) {
                            hourglass[localRow][localCol] = matrix[globalRow][globalCol];
                        } else {
                            hourglass[localRow][localCol] = 0; // filler
                        }
                    }
                }
                hourglasses.add(hourglass);
            }
        }

        return hourglasses;
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int value : row) {
                System.out.printf("%3d", value);
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int matrixSize = 5;
        int hourglassSize = 3;
        int[][] matrix = new int[matrixSize][matrixSize];

        // Fill matrix with values 0..24
        int value = 0;
        for (int i = 0; i < matrixSize; i++) {
            for (int j = 0; j < matrixSize; j++) {
                matrix[i][j] = value++;
            }
        }

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        List<int[][]> hourglasses = extractHourglassBlocks(matrix, hourglassSize);

        int count = 1;
        for (int[][] hourglass : hourglasses) {
            System.out.printf("Hourglass %d:\n", count++);
            printMatrix(hourglass);
        }
    }
}
