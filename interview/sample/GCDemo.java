public class GCDemo {

    private static final int SIZE = 1000000;

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Starting GC demonstration...");

        // Allocate memory by creating objects
        for (int i = 0; i < 5; i++) {
            allocateMemory();
            System.gc(); // Suggest garbage collection
            Thread.sleep(1000); // Sleep to allow GC to run
        }

        System.out.println("GC demonstration completed.");
    }

    private static void allocateMemory() {
        int[] array = new int[SIZE];
        for (int i = 0; i < SIZE; i++) {
            array[i] = i;
        }
        System.out.println("Allocated memory for array of size: " + SIZE);
    }
}
