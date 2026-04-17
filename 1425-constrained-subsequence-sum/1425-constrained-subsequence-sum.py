from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        dq = deque()
        dp = nums[:]  # dp[i] = max sum ending at i
        
        for i in range(len(nums)):
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])
            
            # maintain decreasing deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            if dp[i] > 0:
                dq.append(i)
            
            # remove out of window
            if dq and dq[0] <= i - k:
                dq.popleft()
        
        return max(dp)