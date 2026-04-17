class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [float('inf')] * n
        maxd = 0
        
        # Day 1 initialization
        for i in range(n):
            maxd = max(maxd, jobDifficulty[i])
            dp[i] = maxd
        
        # Fill for days 2 to d
        for day in range(2, d + 1):
            new_dp = [float('inf')] * n
            
            for i in range(day - 1, n):
                maxd = 0
                for j in range(i, day - 2, -1):
                    maxd = max(maxd, jobDifficulty[j])
                    new_dp[i] = min(new_dp[i], dp[j - 1] + maxd)
            
            dp = new_dp
        
        return dp[-1]