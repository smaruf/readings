import java.util.*;

public class WaterHeightProblem {
    public static int[][] assignHeights(int[][] isWater) {
        int rows = isWater.length;
        int cols = isWater[0].length;
        int[][] heights = new int[rows][cols];
        
        // Initialize heights with -1 to mark unvisited cells
        for (int[] row : heights) {
            Arrays.fill(row, -1);
        }
        
        // Use a Queue for BFS
        Queue<int[]> queue = new LinkedList<>();
        
        // Initialize the queue with all water cells and set their height to 0
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (isWater[r][c] == 1) {
                    heights[r][c] = 0;
                    queue.add(new int[]{r, c});
                }
            }
        }
        
        // Directions for moving up, down, left, right
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        // Perform BFS to assign heights
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            int currentHeight = heights[r][c];
            
            for (int[] direction : directions) {
                int nr = r + direction[0];
                int nc = c + direction[1];
                
                // Check bounds and ensure the cell is unvisited
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && heights[nr][nc] == -1) {
                    heights[nr][nc] = currentHeight + 1;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        
        return heights;
    }

    public static void main(String[] args) {
        int[][] isWater = {
            {0, 0, 1},
            {1, 0, 0},
            {0, 0, 0}
        };
        
        int[][] heights = assignHeights(isWater);
        
        // Print the resulting heights matrix
        for (int[] row : heights) {
            System.out.println(Arrays.toString(row));
        }
    }
}