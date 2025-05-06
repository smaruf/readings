import java.util.ArrayList;
import java.util.List;

public class Combinations {
    public static List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>(), result);
        return result;
    }

    private static void backtrack(int start, int n, int k, List<Integer> combination, List<List<Integer>> result) {
        if (combination.size() == k) {
            result.add(new ArrayList<>(combination));
            return;
        }

        for (int i = start; i <= n; i++) {
            // Include the current number in the combination
            combination.add(i);
            backtrack(i + 1, n, k, combination, result);
            // Backtrack: remove the current number
            combination.remove(combination.size() - 1);
        }
    }

    public static void main(String[] args) {
        int n = 4, k = 2;
        List<List<Integer>> combinations = combine(n, k);
        System.out.println(combinations);
        // Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    }
}
