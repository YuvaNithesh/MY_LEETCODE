from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites):
    
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            
            adj[b].append(a)
            in_degree[a] += 1

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        taken = 0 

        while q:
            course = q.popleft()
            taken += 1  
            for nei in adj[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return taken == numCourses
