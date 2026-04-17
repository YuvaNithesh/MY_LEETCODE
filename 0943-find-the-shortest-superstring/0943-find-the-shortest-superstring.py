class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        
        # Step 1: compute overlap cost (extra chars needed)
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    for k in range(min(len(words[i]), len(words[j])), -1, -1):
                        if words[i].endswith(words[j][:k]):
                            overlap[i][j] = len(words[j]) - k
                            break
        
        # Step 2: DP (store length only)
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1 << i][i] = len(words[i])
        
        for mask in range(1 << n):
            for last in range(n):
                if not (mask & (1 << last)):
                    continue
                
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    
                    new_mask = mask | (1 << nxt)
                    new_len = dp[mask][last] + overlap[last][nxt]
                    
                    if new_len < dp[new_mask][nxt]:
                        dp[new_mask][nxt] = new_len
                        parent[new_mask][nxt] = last
        
        # Step 3: find best ending
        full = (1 << n) - 1
        last = min(range(n), key=lambda i: dp[full][i])
        
        # Step 4: reconstruct path
        path = []
        mask = full
        while last != -1:
            path.append(last)
            temp = parent[mask][last]
            mask ^= (1 << last)
            last = temp
        
        path = path[::-1]
        
        # Step 5: build string
        res = words[path[0]]
        for i in range(1, len(path)):
            prev = path[i-1]
            curr = path[i]
            
            # find overlap again
            k = 0
            for l in range(min(len(words[prev]), len(words[curr])), -1, -1):
                if words[prev].endswith(words[curr][:l]):
                    k = l
                    break
            
            res += words[curr][k:]
        
        return res