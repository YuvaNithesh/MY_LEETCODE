class Solution:
    def findGoodStrings(self, n, s1, s2, evil):
        MOD = 10**9 + 7
        
        # build LPS array for KMP
        def build_lps(p):
            lps = [0] * len(p)
            j = 0
            for i in range(1, len(p)):
                while j > 0 and p[i] != p[j]:
                    j = lps[j - 1]
                if p[i] == p[j]:
                    j += 1
                    lps[i] = j
            return lps
        
        lps = build_lps(evil)
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, matched, tight_low, tight_high):
            if matched == len(evil):
                return 0
            if i == n:
                return 1
            
            low = s1[i] if tight_low else 'a'
            high = s2[i] if tight_high else 'z'
            
            res = 0
            for c in range(ord(low), ord(high) + 1):
                ch = chr(c)
                
                j = matched
                while j > 0 and evil[j] != ch:
                    j = lps[j - 1]
                if evil[j] == ch:
                    j += 1
                
                res += dp(
                    i + 1,
                    j,
                    tight_low and ch == low,
                    tight_high and ch == high
                )
                res %= MOD
            
            return res
        
        return dp(0, 0, True, True)