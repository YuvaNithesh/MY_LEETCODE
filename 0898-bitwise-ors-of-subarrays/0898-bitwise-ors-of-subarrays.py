class Solution:
    def subarrayBitwiseORs(self, arr):
        curr = set()
        result = set()
        
        for x in arr:
            curr = {x | y for y in curr} | {x}
            result |= curr
        
        return len(result)