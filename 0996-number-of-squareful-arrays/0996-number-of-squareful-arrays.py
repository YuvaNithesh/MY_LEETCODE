from functools import lru_cache
import math

class Solution:
    def numSquarefulPerms(self, nums):
        nums.sort()
        n = len(nums)
        
        # Precompute valid edges
        graph = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    s = nums[i] + nums[j]
                    if int(math.isqrt(s))**2 == s:
                        graph[i][j] = True
        
        @lru_cache(None)
        def dfs(last, mask):
            if mask == (1 << n) - 1:
                return 1
            
            res = 0
            
            for i in range(n):
                if mask & (1 << i):
                    continue
                
                # skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not (mask & (1 << (i-1))):
                    continue
                
                if last == -1 or graph[last][i]:
                    res += dfs(i, mask | (1 << i))
            
            return res
        
        return dfs(-1, 0)