class Solution:
    def getMaxLen(self, nums):
        pos = 0
        neg = 0
        res = 0
        
        for num in nums:
            if num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            
            elif num < 0:
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            
            else:
                pos = neg = 0
            
            res = max(res, pos)
        
        return res