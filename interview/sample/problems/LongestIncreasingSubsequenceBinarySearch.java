import java.util.ArrayList;
import java.util.List;

public class LongestIncreasingSubsequenceBinarySearch {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        // List to store the smallest tail of all increasing subsequences
        List<Integer> sub = new ArrayList<>();

        for (int num : nums) {
            int pos = binarySearch(sub, num);
            if (pos < sub.size()) {
                sub.set(pos, num); // Replace the existing value
            } else {
                sub.add(num); // Extend the subsequence
            }
        }

        return sub.size();
    }

    private int binarySearch(List<Integer> sub, int target) {
        int left = 0, right = sub.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (sub.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        LongestIncreasingSubsequenceBinarySearch lis = new LongestIncreasingSubsequenceBinarySearch();
        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println("Length of LIS: " + lis.lengthOfLIS(nums));
    }
}
