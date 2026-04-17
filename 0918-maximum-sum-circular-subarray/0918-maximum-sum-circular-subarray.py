class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        
        # Kadane for max
        max_sum = curr_max = nums[0]
        
        # Kadane for min
        min_sum = curr_min = nums[0]
        
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        # Edge case: all negative
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total - min_sum)