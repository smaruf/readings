import java.util.*;

public class TwoStringRemoveIndexV1 {
    
    public static List<Integer> findRemovableIndices(String str1, String str2) {
        if (str1.length() != str2.length() + 1) {
            return Arrays.asList(-1);
        }

        LinkedList<Character> list = new LinkedList<>();
        for (char c : str1.toCharArray()) {
            list.add(c);
        }

        List<Integer> removableIndices = new ArrayList<>();
        for (int i = 0; i < str1.length(); i++) {
            char removed = list.remove(i);
            if (compareWithString(list, str2)) {
                removableIndices.add(i);
            }
            list.add(i, removed); // Restore character
        }

        return removableIndices.isEmpty() ? Arrays.asList(-1) : removableIndices;
    }

    // Helper to compare LinkedList<Character> with String
    private static boolean compareWithString(LinkedList<Character> list, String str) {
        if (list.size() != str.length()) return false;
        Iterator<Character> it = list.iterator();
        for (int i = 0; i < str.length(); i++) {
            if (!it.hasNext() || str.charAt(i) != it.next()) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String str1 = "abdgggda";
        String str2 = "abdggda";

        List<Integer> result = findRemovableIndices(str1, str2);
        System.out.println(result); // Output: [3, 4, 5]
    }
}
