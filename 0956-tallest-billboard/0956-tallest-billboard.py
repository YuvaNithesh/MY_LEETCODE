class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        
        for r in rods:
            cur = dp.copy()
            
            for diff in cur:
                height = cur[diff]
                
                # Add to taller side
                dp[diff + r] = max(dp.get(diff + r, 0), height)
                
                # Add to shorter side
                new_diff = abs(diff - r)
                new_height = height + min(diff, r)
                dp[new_diff] = max(dp.get(new_diff, 0), new_height)
        
        return dp[0]