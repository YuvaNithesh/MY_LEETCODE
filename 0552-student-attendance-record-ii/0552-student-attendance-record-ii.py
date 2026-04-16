class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[a][l]
        dp = [[0]*3 for _ in range(2)]
        dp[0][0] = 1
        
        for _ in range(n):
            new_dp = [[0]*3 for _ in range(2)]
            
            for a in range(2):
                for l in range(3):
                    val = dp[a][l]
                    if val == 0:
                        continue
                    
                    # Add 'P' → reset L
                    new_dp[a][0] = (new_dp[a][0] + val) % MOD
                    
                    # Add 'A' → only if no A used
                    if a == 0:
                        new_dp[1][0] = (new_dp[1][0] + val) % MOD
                    
                    # Add 'L' → only if l < 2
                    if l < 2:
                        new_dp[a][l+1] = (new_dp[a][l+1] + val) % MOD
            
            dp = new_dp
        
        return sum(sum(row) for row in dp) % MOD