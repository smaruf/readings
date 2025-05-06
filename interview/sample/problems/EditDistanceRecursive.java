import java.util.HashMap;
import java.util.Map;

public class EditDistanceRecursive {
    public static int minDistance(String word1, String word2) {
        Map<String, Integer> memo = new HashMap<>();

        return solve(word1, word2, word1.length(), word2.length(), memo);
    }

    private static int solve(String word1, String word2, int i, int j, Map<String, Integer> memo) {
        // Base cases
        if (i == 0) return j; // Insert all remaining characters of word2
        if (j == 0) return i; // Delete all remaining characters of word1

        // Memoization key
        String key = i + "," + j;
        if (memo.containsKey(key)) return memo.get(key);

        // If characters match, no operation is needed
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
            memo.put(key, solve(word1, word2, i - 1, j - 1, memo));
        } else {
            // Consider all operations: insert, delete, replace
            int insert = solve(word1, word2, i, j - 1, memo);
            int delete = solve(word1, word2, i - 1, j, memo);
            int replace = solve(word1, word2, i - 1, j - 1, memo);

            memo.put(key, 1 + Math.min(insert, Math.min(delete, replace)));
        }

        return memo.get(key);
    }

    public static void main(String[] args) {
        String word1 = "horse";
        String word2 = "ros";
        System.out.println(minDistance(word1, word2)); // Output: 3
    }
}
