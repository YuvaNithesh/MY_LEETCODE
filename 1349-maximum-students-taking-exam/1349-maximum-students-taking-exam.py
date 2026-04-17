class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        
        # Precompute valid masks for each row
        valid = []
        for i in range(m):
            masks = []
            for mask in range(1 << n):
                ok = True
                for j in range(n):
                    if (mask & (1 << j)):
                        if seats[i][j] == '#':
                            ok = False
                            break
                        if j > 0 and (mask & (1 << (j - 1))):
                            ok = False
                            break
                if ok:
                    masks.append(mask)
            valid.append(masks)
        
        # dp[row][mask] = max students
        dp = [dict() for _ in range(m)]
        
        for mask in valid[0]:
            dp[0][mask] = bin(mask).count('1')
        
        for i in range(1, m):
            for mask in valid[i]:
                students = bin(mask).count('1')
                for pmask in dp[i-1]:
                    if (mask & (pmask << 1)) == 0 and (mask & (pmask >> 1)) == 0:
                        dp[i][mask] = max(dp[i].get(mask, 0),
                                          dp[i-1][pmask] + students)
        
        return max(dp[m-1].values())