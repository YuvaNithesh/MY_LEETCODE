class Solution:
    def oddEvenJumps(self, arr):
        n = len(arr)
        
        def make_next(indices):
            res = [None] * n
            stack = []
            for i in indices:
                while stack and i > stack[-1]:
                    res[stack.pop()] = i
                stack.append(i)
            return res
        
        # Odd jumps (next greater or equal)
        idx_sorted = sorted(range(n), key=lambda i: (arr[i], i))
        next_higher = make_next(idx_sorted)
        
        # Even jumps (next smaller or equal)
        idx_sorted = sorted(range(n), key=lambda i: (-arr[i], i))
        next_lower = make_next(idx_sorted)
        
        odd = [False] * n
        even = [False] * n
        
        odd[-1] = even[-1] = True
        
        for i in range(n - 2, -1, -1):
            if next_higher[i] is not None:
                odd[i] = even[next_higher[i]]
            if next_lower[i] is not None:
                even[i] = odd[next_lower[i]]
        
        return sum(odd)