class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)
        
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]
        
        def get_sum(i, j):
            return prefix[j+1] - prefix[i]
        
        dp = [[0]*n for _ in range(n)]
        
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                for m in range(i, j, k - 1):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][m] + dp[m+1][j]
                    )
                
                # If can merge into one pile
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += get_sum(i, j)
        
        return dp[0][n-1]