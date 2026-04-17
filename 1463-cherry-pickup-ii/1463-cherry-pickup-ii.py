class Solution:
    def cherryPickup(self, grid):
        m, n = len(grid), len(grid[0])
        
        dp = [[-1]*n for _ in range(n)]
        dp[0][0] = grid[0][0] + (grid[0][n-1] if n > 1 else 0)
        
        # fix initial positions: robot1 at 0, robot2 at n-1
        dp = [[-1]*n for _ in range(n)]
        dp[0][n-1] = grid[0][0] + (grid[0][n-1] if n > 1 else 0)
        
        for i in range(1, m):
            new_dp = [[-1]*n for _ in range(n)]
            
            for j1 in range(n):
                for j2 in range(n):
                    if dp[j1][j2] == -1:
                        continue
                    
                    for dj1 in (-1, 0, 1):
                        for dj2 in (-1, 0, 1):
                            nj1, nj2 = j1 + dj1, j2 + dj2
                            
                            if 0 <= nj1 < n and 0 <= nj2 < n:
                                val = dp[j1][j2] + grid[i][nj1]
                                if nj1 != nj2:
                                    val += grid[i][nj2]
                                
                                new_dp[nj1][nj2] = max(new_dp[nj1][nj2], val)
            
            dp = new_dp
        
        return max(max(row) for row in dp)