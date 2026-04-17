class Solution:
    def minCost(self, houses, cost, m, n, target):
        INF = 10**18
        
        # dp[i][j][k]: min cost for first i houses,
        # ith house painted with color j, forming k neighborhoods
        dp = [[[INF]*(target+1) for _ in range(n+1)] for _ in range(m+1)]
        
        # initialization for first house
        if houses[0] == 0:
            for j in range(1, n+1):
                dp[1][j][1] = cost[0][j-1]
        else:
            dp[1][houses[0]][1] = 0
        
        for i in range(2, m+1):
            for j in range(1, n+1):
                if houses[i-1] != 0 and houses[i-1] != j:
                    continue
                
                paint_cost = 0 if houses[i-1] != 0 else cost[i-1][j-1]
                
                for pj in range(1, n+1):
                    for k in range(1, target+1):
                        if pj == j:
                            dp[i][j][k] = min(
                                dp[i][j][k],
                                dp[i-1][pj][k] + paint_cost
                            )
                        else:
                            if k > 1:
                                dp[i][j][k] = min(
                                    dp[i][j][k],
                                    dp[i-1][pj][k-1] + paint_cost
                                )
        
        res = min(dp[m][j][target] for j in range(1, n+1))
        return -1 if res == INF else res