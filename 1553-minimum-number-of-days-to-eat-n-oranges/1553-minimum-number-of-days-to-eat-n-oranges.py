from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return n
            
            # Option 1: make divisible by 2
            by2 = n % 2 + dp(n // 2)
            
            # Option 2: make divisible by 3
            by3 = n % 3 + dp(n // 3)
            
            return 1 + min(by2, by3)
        
        return dp(n)