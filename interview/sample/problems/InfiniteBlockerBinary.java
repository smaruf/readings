import java.util.*;

public class InfiniteBlockerBinary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder result = new StringBuilder();

        // Read number of test cases (matrices)
        int T = sc.nextInt();
        for (int t = 0; t < T; t++) {
            // Read matrix dimensions
            int n = sc.nextInt();
            int m = sc.nextInt();

            int[][] matrix = new int[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    matrix[i][j] = sc.nextInt();

            // Detect blockers for this matrix
            if (hasBlockers(matrix)) {
                result.append('1');
            } else {
                result.append('0');
            }
        }
        System.out.println(result.toString());
    }

    // Returns true if there is at least one blocker
    static boolean hasBlockers(int[][] matrix) {
        boolean[] blocked = new boolean[100]; // Values 1..99
        boolean found = false;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                int value = matrix[i][j];
                if (!blocked[value]) {
                    blocked[value] = true;
                    found = true;
                }
            }
        }
        return found;
    }
}
