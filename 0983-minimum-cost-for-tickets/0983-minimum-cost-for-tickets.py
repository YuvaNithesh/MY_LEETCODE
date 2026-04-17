from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            
            # 1-day pass
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            cost1 = costs[0] + dp(j)
            
            # 7-day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            cost7 = costs[1] + dp(j)
            
            # 30-day pass
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            cost30 = costs[2] + dp(j)
            
            return min(cost1, cost7, cost30)
        
        return dp(0)