class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        
        prev = grid[0][:]
        
        for i in range(1, n):
            # find smallest and second smallest in prev row
            min1 = min2 = float('inf')
            idx1 = -1
            
            for j in range(n):
                if prev[j] < min1:
                    min2 = min1
                    min1 = prev[j]
                    idx1 = j
                elif prev[j] < min2:
                    min2 = prev[j]
            
            curr = [0] * n
            for j in range(n):
                if j == idx1:
                    curr[j] = grid[i][j] + min2
                else:
                    curr[j] = grid[i][j] + min1
            
            prev = curr
        
        return min(prev)