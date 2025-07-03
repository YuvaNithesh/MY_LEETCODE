class Solution {
    public String reverseVowels(String s) {
        // Define vowels
        String vowels = "aeiouAEIOU";
        char[] chars = s.toCharArray();
        int left = 0, right = chars.length - 1;

        while (left < right) {
            // Move the left pointer to the next vowel
            while (left < right && vowels.indexOf(chars[left]) == -1) {
                left++;
            }
            // Move the right pointer to the previous vowel
            while (left < right && vowels.indexOf(chars[right]) == -1) {
                right--;
            }
            // Swap the vowels
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;

            // Move the pointers inward
            left++;
            right--;
        }

        return new String(chars);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        String s1 = "hello";
        System.out.println(solution.reverseVowels(s1)); // Output: "holle"

        // Example 2
        String s2 = "leetcode";
        System.out.println(solution.reverseVowels(s2)); // Output: "leotcede"

        // Example 3
        String s3 = "aA";
        System.out.println(solution.reverseVowels(s3)); // Output: "Aa"
    }
}
