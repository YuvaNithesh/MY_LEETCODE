class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # two patterns:
        # aba (2 colors same), abc (all different)
        aba = 6   # e.g., 121, 131, etc.
        abc = 6   # e.g., 123, 132, etc.
        
        for _ in range(1, n):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD
            aba, abc = new_aba, new_abc
        
        return (aba + abc) % MOD