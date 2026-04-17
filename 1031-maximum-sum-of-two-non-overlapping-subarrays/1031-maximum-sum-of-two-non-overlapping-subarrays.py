class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        
        def helper(L, M):
            n = len(nums)
            
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i+1] = prefix[i] + nums[i]
            
            max_L = 0
            res = 0
            
            for i in range(L + M, n + 1):
                # best L before M
                max_L = max(max_L, prefix[i-M] - prefix[i-M-L])
                
                # current M
                curr_M = prefix[i] - prefix[i-M]
                
                res = max(res, max_L + curr_M)
            
            return res
        
        return max(
            helper(firstLen, secondLen),
            helper(secondLen, firstLen)
        )