class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        # cost[i][j]: min changes to make s[i..j] a palindrome
        cost = [[0]*n for _ in range(n)]
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
        
        # dp[i][p]: min changes for s[0..i] into p partitions
        dp = [[float('inf')] * (k+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][1] = cost[0][i]
        
        for i in range(n):
            for p in range(2, k+1):
                for j in range(i):
                    dp[i][p] = min(dp[i][p], dp[j][p-1] + cost[j+1][i])
        
        return dp[n-1][k]