class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        
        total = 0
        prefix = 0
        
        for x in reversed(satisfaction):
            prefix += x
            if prefix <= 0:
                break
            total += prefix
        
        return total