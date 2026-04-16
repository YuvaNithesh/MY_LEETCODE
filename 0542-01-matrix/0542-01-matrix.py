from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        # Step 1: Push all 0s into queue, mark 1s as unvisited (-1)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat