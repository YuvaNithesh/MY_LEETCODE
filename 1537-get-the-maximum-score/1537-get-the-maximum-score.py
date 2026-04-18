class Solution:
    def maxSum(self, nums1, nums2):
        MOD = 10**9 + 7
        
        i = j = 0
        sum1 = sum2 = 0
        result = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # Common element
                result += max(sum1, sum2) + nums1[i]
                sum1 = sum2 = 0
                i += 1
                j += 1
        
        # Add remaining
        sum1 += sum(nums1[i:])
        sum2 += sum(nums2[j:])
        
        result += max(sum1, sum2)
        
        return result % MOD