class Solution:
    def minimumDistance(self, word: str) -> int:
        from functools import lru_cache
        
        def dist(a, b):
            if a == -1 or b == -1:
                return 0
            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)
            return abs(ax - bx) + abs(ay - by)
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0
            
            curr = ord(word[i]) - ord('A')
            
            # use finger1
            use_f1 = dist(f1, curr) + dp(i + 1, curr, f2)
            
            # use finger2
            use_f2 = dist(f2, curr) + dp(i + 1, f1, curr)
            
            return min(use_f1, use_f2)
        
        return dp(0, -1, -1)