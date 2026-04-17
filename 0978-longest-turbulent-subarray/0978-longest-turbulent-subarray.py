class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2:
            return n
        
        up = down = 1
        res = 1
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i-1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            
            res = max(res, up, down)
        
        return res