class Solution:
    def minTaps(self, n, ranges):
        intervals = []
        for i, r in enumerate(ranges):
            if r > 0:
                intervals.append((max(0, i - r), min(n, i + r)))
        
        intervals.sort()
        
        res = 0
        i = 0
        curr_end = 0
        farthest = 0
        
        while curr_end < n:
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1])
                i += 1
            
            if farthest == curr_end:
                return -1
            
            res += 1
            curr_end = farthest
        
        return res