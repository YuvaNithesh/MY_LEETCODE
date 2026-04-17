class Solution:
    def numberWays(self, hats):
        MOD = 10**9 + 7
        n = len(hats)
        
        # map hat -> list of people
        hat_to_people = [[] for _ in range(41)]
        for p, hs in enumerate(hats):
            for h in hs:
                hat_to_people[h].append(p)
        
        # dp[mask] = ways
        dp = [0] * (1 << n)
        dp[0] = 1
        
        for h in range(1, 41):
            new_dp = dp[:]
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue
                for p in hat_to_people[h]:
                    if not (mask & (1 << p)):
                        new_mask = mask | (1 << p)
                        new_dp[new_mask] = (new_dp[new_mask] + dp[mask]) % MOD
            dp = new_dp
        
        return dp[(1 << n) - 1]