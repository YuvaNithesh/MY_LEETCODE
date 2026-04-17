class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[i][j] = (max_score, ways)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue
                
                candidates = []
                if i + 1 < n:
                    candidates.append(dp[i+1][j])
                if j + 1 < n:
                    candidates.append(dp[i][j+1])
                if i + 1 < n and j + 1 < n:
                    candidates.append(dp[i+1][j+1])
                
                max_score = max([c[0] for c in candidates])
                if max_score < 0:
                    continue
                
                ways = sum(c[1] for c in candidates if c[0] == max_score) % MOD
                
                val = 0 if board[i][j] in 'SE' else int(board[i][j])
                dp[i][j] = (max_score + val, ways)
        
        score, ways = dp[0][0]
        return [0, 0] if score < 0 else [score, ways]