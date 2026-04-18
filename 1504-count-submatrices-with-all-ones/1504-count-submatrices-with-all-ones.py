class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        res = 0
        
        for i in range(m):
            # Step 1: Build heights
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Step 2: Monotonic stack
            stack = []
            dp = [0] * n
            
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                
                if stack:
                    prev = stack[-1]
                    dp[j] = dp[prev] + heights[j] * (j - prev)
                else:
                    dp[j] = heights[j] * (j + 1)
                
                stack.append(j)
                res += dp[j]
        
        return res