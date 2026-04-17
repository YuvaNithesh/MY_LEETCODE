class Solution:
    def ways(self, pizza, k):
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        
        # prefix sum: apples from (i,j) to bottom-right
        pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                pre[i][j] = (
                    (pizza[i][j] == 'A')
                    + pre[i+1][j]
                    + pre[i][j+1]
                    - pre[i+1][j+1]
                )
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, j, cuts):
            if pre[i][j] == 0:
                return 0
            if cuts == 1:
                return 1
            
            res = 0
            
            # horizontal cuts
            for x in range(i+1, m):
                if pre[i][j] - pre[x][j] > 0:
                    res = (res + dp(x, j, cuts-1)) % MOD
            
            # vertical cuts
            for y in range(j+1, n):
                if pre[i][j] - pre[i][y] > 0:
                    res = (res + dp(i, y, cuts-1)) % MOD
            
            return res
        
        return dp(0, 0, k)