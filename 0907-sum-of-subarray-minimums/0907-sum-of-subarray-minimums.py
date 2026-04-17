class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        
        stack = []
        left = [0] * n
        
        # Previous Less (strict)
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count
        
        stack = []
        right = [0] * n
        
        # Next Less or Equal
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count
        
        result = 0
        for i in range(n):
            result += arr[i] * left[i] * right[i]
            result %= MOD
        
        return result