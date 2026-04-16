class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                dp[i][j] = 1 + dp[i+1][j]
                
                for k in range(i+1, j+1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j],
                                       dp[i][k-1] + (dp[k+1][j] if k+1 <= j else 0))
        
        return dp[0][n-1]