import java.util.Arrays;

public class CoinChange {
    public static int coinChange(int[] coins, int amount) {
        // Initialize DP array with a large value (infinity)
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0; // Base case: 0 coins needed for amount 0

        // Update DP table
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        // If dp[amount] is still greater than amount, return -1 (not possible to make the amount)
        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;
        int result = coinChange(coins, amount);
        System.out.println(result); // Output: 3 (5 + 5 + 1)
    }
}
