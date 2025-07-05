import java.util.ArrayList;
import java.util.List;

public class RegenerativeEliminationSimulation {

    public static Result processUntilNoA(List<String> arr, int counterStep) {
        int iteration = 0;
        while (arr.contains("A")) {
            iteration++;
            System.out.println("\nIteration " + iteration + " - Start: " + arr);

            // Step 1: Remove up to counterStep 'P's from the end
            int pRemoved = 0;
            for (int i = arr.size() - 1; i >= 0; i--) {
                if (arr.get(i).equals("P")) {
                    arr.remove(i);
                    pRemoved++;
                    if (pRemoved == counterStep) {
                        break;
                    }
                }
            }

            // Step 2: Remove up to counterStep 'A's from the end
            int aRemoved = 0;
            for (int i = arr.size() - 1; i >= 0; i--) {
                if (arr.get(i).equals("A")) {
                    arr.remove(i);
                    aRemoved++;
                    if (aRemoved == counterStep) {
                        break;
                    }
                }
            }

            // Step 3: Add 'A's at the beginning equal to number of P's removed
            for (int i = 0; i < pRemoved; i++) {
                arr.add(0, "A");
            }

            System.out.println("Removed " + pRemoved + " 'P'(s), " + aRemoved + " 'A'(s), Added " + pRemoved + " 'A'(s) at start.");
            System.out.println("Iteration " + iteration + " - End: " + arr);

            // Safety check to avoid infinite loop if it's regenerating forever
            if (pRemoved == 0 && aRemoved == 0) {
                System.out.println("No changes in this iteration. Breaking to prevent infinite loop.");
                break;
            }
        }

        System.out.println("\nFinal array after " + iteration + " iterations: " + arr);
        return new Result(arr, iteration);
    }

    public static void main(String[] args) {
        List<String> initialArray = new ArrayList<>();
        initialArray.add("A");
        initialArray.add("A");
        initialArray.add("A");
        initialArray.add("P");
        initialArray.add("P");
        initialArray.add("P");
        int counterStep = 2;

        Result result = processUntilNoA(initialArray, counterStep);
        // result.finalArray and result.totalIterations available for further use
    }

    // Helper class for returning multiple values
    static class Result {
        List<String> finalArray;
        int totalIterations;

        Result(List<String> finalArray, int totalIterations) {
            this.finalArray = finalArray;
            this.totalIterations = totalIterations;
        }
    }
}
