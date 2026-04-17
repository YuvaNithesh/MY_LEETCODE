class Solution:
    def getKth(self, lo, hi, k):
        from functools import lru_cache
        
        @lru_cache(None)
        def power(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + power(x // 2)
            else:
                return 1 + power(3 * x + 1)
        
        arr = [(power(x), x) for x in range(lo, hi + 1)]
        arr.sort()
        
        return arr[k - 1][1]