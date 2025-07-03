class Solution {
    public int maxVowels(String s, int k) {
        int maxVowels = 0;
        int currentVowels = 0;
        int vowelCount = 0;
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        // Initialize the count of vowels in the first window (first substring of length k)
        for (int i = 0; i < k; i++) {
            if (vowels.contains(s.charAt(i))) {
                currentVowels++;
            }
        }
        maxVowels = currentVowels;

        // Slide the window across the string
        for (int i = k; i < s.length(); i++) {
            // Remove the first character of the previous window if it's a vowel
            if (vowels.contains(s.charAt(i - k))) {
                currentVowels--;
            }
            // Add the new character of the current window if it's a vowel
            if (vowels.contains(s.charAt(i))) {
                currentVowels++;
            }
            // Update the maximum vowels count
            maxVowels = Math.max(maxVowels, currentVowels);
        }

        return maxVowels;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        String s1 = "abciiidef";
        int k1 = 3;
        System.out.println(solution.maxVowels(s1, k1)); // Output: 3

        // Example 2
        String s2 = "aeiou";
        int k2 = 2;
        System.out.println(solution.maxVowels(s2, k2)); // Output: 2

        // Example 3
        String s3 = "leetcode";
        int k3 = 3;
        System.out.println(solution.maxVowels(s3, k3)); // Output: 2
    }
}
