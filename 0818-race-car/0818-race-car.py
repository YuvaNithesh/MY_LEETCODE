class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        
        for t in range(1, target + 1):
            k = t.bit_length()
            
            # Exact reach
            if (1 << k) - 1 == t:
                dp[t] = k
                continue
            
            # Overshoot
            dp[t] = k + 1 + dp[(1 << k) - 1 - t]
            
            # Undershoot
            for m in range(k - 1):
                dist = (1 << (k - 1)) - 1
                back = (1 << m) - 1
                
                dp[t] = min(
                    dp[t],
                    (k - 1) + 1 + m + 1 + dp[t - dist + back]
                )
        
        return dp[target]