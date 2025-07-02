class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int i = 0, j = 0;

        // Merge the strings alternately
        while (i < word1.length() && j < word2.length()) {
            merged.append(word1.charAt(i));
            merged.append(word2.charAt(j));
            i++;
            j++;
        }

        // Append the remaining characters from the longer string
        if (i < word1.length()) {
            merged.append(word1.substring(i));
        }
        if (j < word2.length()) {
            merged.append(word2.substring(j));
        }

        return merged.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        String word1 = "abc";
        String word2 = "pqr";
        System.out.println(solution.mergeAlternately(word1, word2)); // Output: "apbqcr"

        // Example 2
        word1 = "ab";
        word2 = "pqrs";
        System.out.println(solution.mergeAlternately(word1, word2)); // Output: "apbqrs"

        // Example 3
        word1 = "abcd";
        word2 = "pq";
        System.out.println(solution.mergeAlternately(word1, word2)); // Output: "apbqcd"
    }
}
