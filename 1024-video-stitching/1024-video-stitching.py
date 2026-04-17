class Solution:
    def videoStitching(self, clips, time):
        max_end = [0] * (time + 1)
        
        for start, end in clips:
            if start <= time:
                max_end[start] = max(max_end[start], end)
        
        res = 0
        curr_end = 0
        farthest = 0
        
        for t in range(time):
            farthest = max(farthest, max_end[t])
            
            if t == curr_end:
                if farthest <= t:
                    return -1
                res += 1
                curr_end = farthest
        
        return res