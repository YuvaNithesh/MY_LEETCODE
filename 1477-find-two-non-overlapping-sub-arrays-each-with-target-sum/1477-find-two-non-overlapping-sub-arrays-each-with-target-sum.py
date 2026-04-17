class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        
        best = [INF] * n  # best[i]: min length of valid subarray ending at or before i
        curr_sum = 0
        left = 0
        res = INF
        min_len = INF
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                length = right - left + 1
                
                if left > 0 and best[left - 1] != INF:
                    res = min(res, length + best[left - 1])
                
                min_len = min(min_len, length)
            
            best[right] = min_len
        
        return res if res != INF else -1