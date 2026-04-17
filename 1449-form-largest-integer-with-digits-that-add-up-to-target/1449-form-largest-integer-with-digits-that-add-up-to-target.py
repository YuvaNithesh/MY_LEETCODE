class Solution:
    def largestNumber(self, cost, target):
        dp = [-10**9] * (target + 1)
        dp[0] = 0
        
        for t in range(1, target + 1):
            for d in range(9):
                if t >= cost[d]:
                    dp[t] = max(dp[t], dp[t - cost[d]] + 1)
        
        if dp[target] < 0:
            return "0"
        
        res = []
        t = target
        
        for d in range(8, -1, -1):
            while t >= cost[d] and dp[t] == dp[t - cost[d]] + 1:
                res.append(str(d + 1))
                t -= cost[d]
        
        return ''.join(res)