import java.util.*;

public class WordBreakBFS {
    public static boolean wordBreak(String s, List<String> wordDict) {
        // Convert the word dictionary to a set for O(1) lookup
        Set<String> wordSet = new HashSet<>(wordDict);

        // BFS queue to store the start indices
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);

        // Visited set to avoid processing the same index multiple times
        Set<Integer> visited = new HashSet<>();

        // Perform the BFS
        while (!queue.isEmpty()) {
            int start = queue.poll();

            // If we've already visited this index, skip it
            if (visited.contains(start)) {
                continue;
            }

            // Mark this index as visited
            visited.add(start);

            // Try every possible substring starting from `start`
            for (int end = start + 1; end <= s.length(); end++) {
                // If the substring is in the dictionary
                if (wordSet.contains(s.substring(start, end))) {
                    // If we've reached the end of the string, return true
                    if (end == s.length()) {
                        return true;
                    }
                    // Otherwise, add the next index to the queue
                    queue.add(end);
                }
            }
        }

        // If we exhaust the queue and don't reach the end, return false
        return false;
    }

    public static void main(String[] args) {
        String s = "leetcode";
        List<String> wordDict = Arrays.asList("leet", "code");
        System.out.println(wordBreak(s, wordDict)); // Output: true
    }
}
