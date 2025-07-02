class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // If concatenating in both orders doesn't yield the same result, there is no common divisor
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }

        // Find the greatest common divisor of the lengths of the strings
        int gcdLength = gcd(str1.length(), str2.length());
        return str1.substring(0, gcdLength);
    }

    // Helper method to compute the GCD of two numbers
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        String str1 = "ABCABC";
        String str2 = "ABC";
        System.out.println(solution.gcdOfStrings(str1, str2)); // Output: "ABC"

        // Example 2
        str1 = "ABABAB";
        str2 = "ABAB";
        System.out.println(solution.gcdOfStrings(str1, str2)); // Output: "AB"

        // Example 3
        str1 = "LEET";
        str2 = "CODE";
        System.out.println(solution.gcdOfStrings(str1, str2)); // Output: ""
    }
}
