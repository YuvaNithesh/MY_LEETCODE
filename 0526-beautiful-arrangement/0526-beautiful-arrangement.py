class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        
        def backtrack(pos):
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % pos == 0 or pos % num == 0):
                    visited[num] = True
                    count += backtrack(pos + 1)
                    visited[num] = False
            
            return count
        
        return backtrack(1)