class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        k = len(s)
        d = len(digits)
        
        # Step 1: smaller length numbers
        total = 0
        for i in range(1, k):
            total += d ** i
        
        # Step 2: same length
        for i in range(k):
            smaller = sum(1 for digit in digits if digit < s[i])
            total += smaller * (d ** (k - i - 1))
            
            if s[i] not in digits:
                return total
        
        # If fully matched
        return total + 1