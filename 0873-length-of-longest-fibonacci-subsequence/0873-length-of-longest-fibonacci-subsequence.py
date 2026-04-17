class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        
        dp = [[2]*n for _ in range(n)]
        max_len = 0
        
        for k in range(n):
            for j in range(k):
                i_val = arr[k] - arr[j]
                
                if i_val < arr[j] and i_val in index:
                    i = index[i_val]
                    dp[j][k] = dp[i][j] + 1
                    max_len = max(max_len, dp[j][k])
        
        return max_len if max_len >= 3 else 0