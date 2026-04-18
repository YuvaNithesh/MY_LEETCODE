class Solution:
    def minCost(self, colors, neededTime):
        res = 0
        max_time = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # remove the smaller one
                res += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]
        
        return res