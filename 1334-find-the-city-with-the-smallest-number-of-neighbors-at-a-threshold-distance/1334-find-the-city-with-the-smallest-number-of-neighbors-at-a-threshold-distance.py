class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        INF = float('inf')
        
        # Initialize distance matrix
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        result_city = -1
        min_reachable = float('inf')
        
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            
            # choose city with smallest count, break tie with larger index
            if count <= min_reachable:
                min_reachable = count
                result_city = i
        
        return result_city