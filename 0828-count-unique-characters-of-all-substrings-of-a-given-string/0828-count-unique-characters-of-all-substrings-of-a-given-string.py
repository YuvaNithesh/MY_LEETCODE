class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c: [-1, -1] for c in set(s)}
        result = 0
        
        for i, ch in enumerate(s):
            prev, last = index[ch]
            
            result += (last - prev) * (i - last)
            
            index[ch] = [last, i]
        
        n = len(s)
        
        for ch in index:
            prev, last = index[ch]
            result += (last - prev) * (n - last)
        
        return result