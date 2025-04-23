public class ClimbingStairs {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        // Initialize the first two steps
        int prev = 1, curr = 2;

        for (int i = 3; i <= n; i++) {
            // Update steps iteratively
            int next = prev + curr;
            prev = curr;
            curr = next;
        }

        return curr;
    }

    public static void main(String[] args) {
        ClimbingStairs solution = new ClimbingStairs();
        int n = 5; // Number of steps
        System.out.println("Number of ways to climb " + n + " steps: " + solution.climbStairs(n));
    }
}
