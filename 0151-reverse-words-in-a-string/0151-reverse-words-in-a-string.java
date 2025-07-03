class Solution {
    public String reverseWords(String s) {
        // Trim leading and trailing spaces and split the string by spaces
        String[] words = s.trim().split("\\s+");
        StringBuilder reversed = new StringBuilder();

        // Iterate over the words in reverse order
        for (int i = words.length - 1; i >= 0; i--) {
            reversed.append(words[i]);
            if (i > 0) {
                reversed.append(" "); // Add a space between words
            }
        }

        return reversed.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        String s1 = "the sky is blue";
        System.out.println(solution.reverseWords(s1)); // Output: "blue is sky the"

        // Example 2
        String s2 = "  hello world  ";
        System.out.println(solution.reverseWords(s2)); // Output: "world hello"

        // Example 3
        String s3 = "a good   example";
        System.out.println(solution.reverseWords(s3)); // Output: "example good a"
    }
}
