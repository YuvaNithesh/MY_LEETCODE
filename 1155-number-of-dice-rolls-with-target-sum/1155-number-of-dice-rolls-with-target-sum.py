class Solution:
    def numRollsToTarget(self, n, k, target):
        MOD = 10**9 + 7
        
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for s in range(1, target+1):
                for face in range(1, k+1):
                    if s - face >= 0:
                        dp[i][s] += dp[i-1][s-face]
                dp[i][s] %= MOD
        
        return dp[n][target]