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
