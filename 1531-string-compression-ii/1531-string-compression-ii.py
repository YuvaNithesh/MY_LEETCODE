from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def get_len(cnt):
            if cnt == 1:
                return 1
            elif cnt < 10:
                return 2
            elif cnt < 100:
                return 3
            else:
                return 4
        
        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return float('inf')
            if i >= len(s):
                return 0
            
            # Option 1: delete
            res = dp(i + 1, k - 1)
            
            # Option 2: keep
            count = 0
            deletions = 0
            
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    count += 1
                else:
                    deletions += 1
                
                if deletions > k:
                    break
                
                res = min(res, get_len(count) + dp(j + 1, k - deletions))
            
            return res
        
        return dp(0, k)