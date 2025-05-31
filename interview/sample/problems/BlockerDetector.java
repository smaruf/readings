import java.util.ArrayList;
import java.util.List;

public class BlockerDetector {

    public static List<int[]> detectBlockers(int[][] matrix) {
        List<int[]> blockers = new ArrayList<>();
        boolean[] blocked = new boolean[100]; // Assuming values are between 1 and 99

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                int value = matrix[i][j];
                if (!blocked[value]) {
                    blockers.add(new int[]{i, j});
                    blocked[value] = true;
                }
            }
        }

        return blockers;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2},
            {1, 6},
            {1, 5, 3},
            {1, 7, 8}
        };

        List<int[]> blockers = detectBlockers(matrix);

        System.out.println("Blockers found at positions:");
        for (int[] pos : blockers) {
            System.out.println("Row: " + pos[0] + ", Column: " + pos[1]);
        }
    }
}
