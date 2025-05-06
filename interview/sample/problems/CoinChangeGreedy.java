import java.util.Arrays;

public class CoinChangeGreedy {
    public static int coinChangeGreedy(int[] coins, int amount) {
        // Sort coins in descending order
        Arrays.sort(coins);
        int n = coins.length;

        int count = 0; // Count of coins used

        for (int i = n - 1; i >= 0; i--) {
            if (amount == 0) break;

            // Use as many coins of the current denomination as possible
            if (coins[i] <= amount) {
                count += amount / coins[i];
                amount %= coins[i];
            }
        }

        // If amount is not zero, it's not possible to make the change
        return amount == 0 ? count : -1;
    }

    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;
        int result = coinChangeGreedy(coins, amount);
        System.out.println(result); // Output: 3 (5 + 5 + 1)
    }
}
