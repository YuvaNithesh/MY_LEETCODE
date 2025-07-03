class Solution {
    public boolean isSubsequence(String s, String t) {
        int sIndex = 0;  // Pointer for string s
        int tIndex = 0;  // Pointer for string t

        // Traverse both strings
        while (sIndex < s.length() && tIndex < t.length()) {
            if (s.charAt(sIndex) == t.charAt(tIndex)) {
                sIndex++;  // Move to the next character in s
            }
            tIndex++;  // Always move to the next character in t
        }

        // If sIndex reached the end of s, it means all characters of s were found in t
        return sIndex == s.length();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        String s1 = "abc";
        String t1 = "ahbgdc";
        System.out.println(solution.isSubsequence(s1, t1)); // Output: true

        // Example 2
        String s2 = "axc";
        String t2 = "ahbgdc";
        System.out.println(solution.isSubsequence(s2, t2)); // Output: false
    }
}
