from collections import deque

class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        
        res = [0] * (n - 1)
        
        # BFS helper
        def bfs(start, nodes_set):
            visited = set([start])
            queue = deque([(start, 0)])
            farthest = (start, 0)
            
            while queue:
                node, dist = queue.popleft()
                farthest = (node, dist)
                
                for nei in graph[node]:
                    if nei in nodes_set and nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))
            
            return farthest, visited
        
        # Iterate all subsets
        for mask in range(1, 1 << n):
            nodes = [i for i in range(n) if mask & (1 << i)]
            
            if len(nodes) < 2:
                continue
            
            nodes_set = set(nodes)
            
            # Check connectivity
            _, visited = bfs(nodes[0], nodes_set)
            if len(visited) != len(nodes):
                continue
            
            # Find diameter
            u, _ = bfs(nodes[0], nodes_set)[0]
            v, diameter = bfs(u, nodes_set)[0]
            
            res[diameter - 1] += 1
        
        return res