class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        
        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        # dp[i] = best for first i elements
        dp = [0.0] * (n + 1)
        
        # Base case: 1 group
        for i in range(1, n + 1):
            dp[i] = prefix[i] / i
        
        # For k groups
        for _ in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            
            for i in range(1, n + 1):
                for j in range(i):
                    new_dp[i] = max(
                        new_dp[i],
                        dp[j] + (prefix[i] - prefix[j]) / (i - j)
                    )
            
            dp = new_dp
        
        return dp[n]