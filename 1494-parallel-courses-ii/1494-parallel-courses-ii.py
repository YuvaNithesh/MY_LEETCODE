from collections import deque

class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        # Step 1: Build prerequisite bitmask
        prereq = [0] * n
        for u, v in relations:
            prereq[v - 1] |= (1 << (u - 1))
        
        # Step 2: BFS
        queue = deque([(0, 0)])  # (mask, semesters)
        visited = set([0])
        
        while queue:
            mask, steps = queue.popleft()
            
            # If all courses taken
            if mask == (1 << n) - 1:
                return steps
            
            # Step 3: Find available courses
            can_take = 0
            for i in range(n):
                if not (mask & (1 << i)) and (prereq[i] & mask) == prereq[i]:
                    can_take |= (1 << i)
            
            # Step 4: Generate subsets of size ≤ k
            subset = can_take
            valid_subsets = []
            
            while subset:
                if bin(subset).count('1') <= k:
                    valid_subsets.append(subset)
                subset = (subset - 1) & can_take
            
            # Optimization: if available courses ≤ k, take all
            if bin(can_take).count('1') <= k:
                valid_subsets = [can_take]
            
            # Step 5: BFS transition
            for sub in valid_subsets:
                new_mask = mask | sub
                if new_mask not in visited:
                    visited.add(new_mask)
                    queue.append((new_mask, steps + 1))
        
        return -1