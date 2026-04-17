class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)
        
        # cost[i][j]: minimum distance to cover houses[i..j] with 1 mailbox
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                for x in range(i, j+1):
                    cost[i][j] += abs(houses[x] - houses[mid])
        
        # dp[i][m]: min cost to cover first i houses with m mailboxes
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for m in range(1, k + 1):
                for j in range(i):
                    dp[i][m] = min(dp[i][m], dp[j][m-1] + cost[j][i-1])
        
        return dp[n][k]