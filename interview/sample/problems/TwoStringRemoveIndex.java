import java.util.*;
import java.util.stream.*;

public class TwoStringRemoveIndex {
    
    public static List<Integer> findRemovableIndices(String str1, String str2) {
        if (str1.length() != str2.length() + 1) {
            return Arrays.asList(-1);
        }

        LinkedList<Character> list = str1.chars()
            .mapToObj(c -> (char) c)
            .collect(Collectors.toCollection(LinkedList::new));

        return IntStream.range(0, str1.length())
            .filter(i -> {
                char removed = list.remove(i);
                boolean matches = compareWithString(list, str2);
                list.add(i, removed); // Restore character
                return matches;
            })
            .boxed()
            .collect(Collectors.collectingAndThen(
                Collectors.toList(),
                l -> l.isEmpty() ? Arrays.asList(-1) : l
            ));
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
