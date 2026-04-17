from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        target = (1 << n) - 1
        
        queue = deque()
        visited = set()
        
        # Start from all nodes
        for i in range(n):
            mask = (1 << i)
            queue.append((i, mask, 0))
            visited.add((i, mask))
        
        while queue:
            node, mask, dist = queue.popleft()
            
            if mask == target:
                return dist
            
            for nei in graph[node]:
                new_mask = mask | (1 << nei)
                
                if (nei, new_mask) not in visited:
                    visited.add((nei, new_mask))
                    queue.append((nei, new_mask, dist + 1))