class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        
        even_count = 1  # empty prefix
        odd_count = 0
        res = 0
        prefix = 0
        
        for num in arr:
            prefix += num
            
            if prefix % 2 == 0:
                res += odd_count
                even_count += 1
            else:
                res += even_count
                odd_count += 1
            
            res %= MOD
        
        return res