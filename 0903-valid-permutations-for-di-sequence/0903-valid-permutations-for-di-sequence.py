class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        dp = [1] * (n + 1)
        
        for i in range(n):
            new = [0] * (n + 1)
            
            if s[i] == 'I':
                curr = 0
                for j in range(n - i):
                    curr = (curr + dp[j]) % MOD
                    new[j] = curr
            else:  # 'D'
                curr = 0
                for j in range(n - i - 1, -1, -1):
                    curr = (curr + dp[j + 1]) % MOD
                    new[j] = curr
            
            dp = new
        
        return dp[0]