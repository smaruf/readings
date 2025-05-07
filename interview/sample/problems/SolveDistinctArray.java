// Input : A[] = {1, 5, 3, 8, 1}
//         B[] = {5, 4, 6, 7}
// Output : 28
// 3 + 4 + 7 + 6 + 8 = 28
 
// Input : A[] = {1, 5, 3, 8}
//         B[] = {5, 1, 8, 3}
// Output : 0

class SolveDistinctArray {
    public static int solve(int[] A, int[] B) {
        int n = A.length;
        int m = B.length;
        int[][] dp = new int[n + 1][m + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (A[i - 1] == B[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + A[i - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[n][m];
    }

    public static void main(String[] args) {
        int[] A = {1, 5, 3, 8, 1};
        int[] B = {5, 4, 6, 7};
        System.out.println(solve(A, B)); // Output: 28
    }
}
