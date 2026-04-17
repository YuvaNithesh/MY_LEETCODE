from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        
        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                
                dp[j][diff] = dp[i][diff] + 1 if diff in dp[i] else 2
                res = max(res, dp[j][diff])
        
        return res