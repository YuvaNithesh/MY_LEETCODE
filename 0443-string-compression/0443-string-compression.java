class Solution {
    public int compress(char[] chars) {
        int write = 0; // Index to write the compressed characters
        int read = 0;  // Index to read the characters

        while (read < chars.length) {
            char currentChar = chars[read];
            int count = 0;

            // Count occurrences of the current character
            while (read < chars.length && chars[read] == currentChar) {
                read++;
                count++;
            }

            // Write the character
            chars[write++] = currentChar;

            // Write the count if greater than 1
            if (count > 1) {
                for (char c : Integer.toString(count).toCharArray()) {
                    chars[write++] = c;
                }
            }
        }

        return write; // New length of the compressed array
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        char[] chars1 = {'a', 'a', 'b', 'b', 'c', 'c', 'c'};
        System.out.println(solution.compress(chars1)); // Output: 6

        // Example 2
        char[] chars2 = {'a'};
        System.out.println(solution.compress(chars2)); // Output: 1

        // Example 3
        char[] chars3 = {'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'};
        System.out.println(solution.compress(chars3)); // Output: 4
    }
}
