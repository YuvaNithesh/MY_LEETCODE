from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        
        DRAW, MOUSE, CAT = 0, 1, 2
        
        dp = [[[DRAW]*2 for _ in range(n)] for _ in range(n)]
        degree = [[[0]*2 for _ in range(n)] for _ in range(n)]
        
        # Initialize degrees
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len(graph[c])
                if 0 in graph[c]:
                    degree[m][c][1] -= 1
        
        queue = deque()
        
        # Terminal states
        for i in range(n):
            for t in range(2):
                if i != 0:
                    dp[0][i][t] = MOUSE
                    queue.append((0, i, t, MOUSE))
                    
                    dp[i][i][t] = CAT
                    queue.append((i, i, t, CAT))
        
        # Reverse BFS
        while queue:
            m, c, turn, result = queue.popleft()
            
            prev_turn = 1 - turn
            
            if prev_turn == 0:  # Mouse turn before
                for pm in graph[m]:
                    if dp[pm][c][prev_turn] != DRAW:
                        continue
                    
                    if result == MOUSE:
                        dp[pm][c][prev_turn] = MOUSE
                        queue.append((pm, c, prev_turn, MOUSE))
                    else:
                        degree[pm][c][prev_turn] -= 1
                        if degree[pm][c][prev_turn] == 0:
                            dp[pm][c][prev_turn] = CAT
                            queue.append((pm, c, prev_turn, CAT))
            
            else:  # Cat turn before
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    
                    if dp[m][pc][prev_turn] != DRAW:
                        continue
                    
                    if result == CAT:
                        dp[m][pc][prev_turn] = CAT
                        queue.append((m, pc, prev_turn, CAT))
                    else:
                        degree[m][pc][prev_turn] -= 1
                        if degree[m][pc][prev_turn] == 0:
                            dp[m][pc][prev_turn] = MOUSE
                            queue.append((m, pc, prev_turn, MOUSE))
        
        return dp[1][2][0]