public class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        // dp[i][j] indicates whether s[0:i] matches p[0:j]
        boolean[][] dp = new boolean[m + 1][n + 1];
        
        // Empty pattern matches empty string.
        dp[0][0] = true;
        
        // Initialize dp for patterns like a* or a*b* that can match an empty string.
        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*' && dp[0][j - 2]) {
                dp[0][j] = true;
            }
        }
        
        // Fill the DP table.
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                char sc = s.charAt(i - 1);
                char pc = p.charAt(j - 1);
                
                if (pc == '*') {
                    // Case 1: Treat '*' as representing zero occurrences.
                    dp[i][j] = dp[i][j - 2];
                    // Case 2: If preceding character matches s[i-1] (or is '.'),
                    // then '*' can match one more character.
                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == sc) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                } else {
                    // Direct match or '.' wildcard.
                    if (pc == '.' || pc == sc) {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Optional main method for quick testing
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "aab";
        String p = "c*a*b";
        System.out.println(sol.isMatch(s, p)); // Expected output: true
    }
}