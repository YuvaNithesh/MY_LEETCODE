class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [0] * n
        
        # sort indices by value
        indices = sorted(range(n), key=lambda x: arr[x])
        
        for i in indices:
            dp[i] = 1
            
            # check left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
            
            # check right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)