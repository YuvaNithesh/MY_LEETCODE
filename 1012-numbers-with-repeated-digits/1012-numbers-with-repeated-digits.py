class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        k = len(s)
        
        # count unique digits
        def count_unique(n):
            digits = list(map(int, str(n)))
            k = len(digits)
            res = 0
            
            # 1. count numbers with fewer digits
            for i in range(1, k):
                count = 9
                available = 9
                for _ in range(i - 1):
                    count *= available
                    available -= 1
                res += count
            
            # 2. same length
            used = set()
            for i in range(k):
                for d in range(0 if i else 1, digits[i]):
                    if d in used:
                        continue
                    
                    count = 1
                    available = 10 - (i + 1)
                    for _ in range(k - i - 1):
                        count *= available
                        available -= 1
                    
                    res += count
                
                if digits[i] in used:
                    break
                used.add(digits[i])
            else:
                res += 1  # include n itself if unique
            
            return res
        
        return n - count_unique(n)