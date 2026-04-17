class Solution:
    def minDeletionSize(self, strs):
        m = len(strs)
        n = len(strs[0])
        
        dp = [1] * n
        
        for j in range(n):
            for i in range(j):
                valid = True
                for r in range(m):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break
                
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return n - max(dp)