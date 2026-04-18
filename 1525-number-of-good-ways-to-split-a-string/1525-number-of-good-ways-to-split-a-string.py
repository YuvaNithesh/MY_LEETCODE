class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        
        left = [0] * n
        right = [0] * n
        
        seen = set()
        for i in range(n):
            seen.add(s[i])
            left[i] = len(seen)
        
        seen.clear()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            right[i] = len(seen)
        
        res = 0
        for i in range(n - 1):
            if left[i] == right[i + 1]:
                res += 1
        
        return res