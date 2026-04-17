class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[c][j] = ways with cost c and max value j
        dp = [[0] * (m + 1) for _ in range(k + 1)]
        
        for j in range(1, m + 1):
            dp[1][j] = 1
        
        for _ in range(2, n + 1):
            new_dp = [[0] * (m + 1) for _ in range(k + 1)]
            
            for c in range(1, k + 1):
                prefix = 0
                for j in range(1, m + 1):
                    # extend without increasing max
                    new_dp[c][j] = (new_dp[c][j] + dp[c][j] * j) % MOD
                    
                    # increase max (use prefix sum)
                    prefix = (prefix + dp[c - 1][j - 1]) % MOD
                    new_dp[c][j] = (new_dp[c][j] + prefix) % MOD
            
            dp = new_dp
        
        return sum(dp[k]) % MOD