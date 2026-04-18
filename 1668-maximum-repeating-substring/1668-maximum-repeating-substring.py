class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        cur = word
        
        while cur in sequence:
            k += 1
            cur += word
        
        return k