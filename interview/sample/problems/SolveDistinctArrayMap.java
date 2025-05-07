import java.util.HashMap;
import java.util.Map;

class SolveDistinctArray {
    public static int solveWithHashMap(int[] A, int[] B) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        // Count occurrences of elements in array A
        for (int num : A) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Count occurrences of elements in array B
        for (int num : B) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Calculate the sum of elements that appear only once
        int sum = 0;
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() == 1) { // Element appears only once
                sum += entry.getKey();
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        int[] A = {1, 5, 3, 8, 1};
        int[] B = {5, 4, 6, 7};
        System.out.println(solveWithHashMap(A, B)); // Output: 28
    }
}
