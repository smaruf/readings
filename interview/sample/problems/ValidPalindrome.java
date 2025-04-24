public class ValidPalindrome {

    public static boolean isPalindrome(String s) {
        // Use two pointers
        int left = 0, right = s.length() - 1;

        while (left < right) {
            // Move left pointer to the next alphanumeric character
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            // Move right pointer to the previous alphanumeric character
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // Compare the characters, ignoring case
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    public static void main(String[] args) {
        // Example usage
        String s1 = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s1)); // Output: true

        String s2 = "race a car";
        System.out.println(isPalindrome(s2)); // Output: false
    }
}
