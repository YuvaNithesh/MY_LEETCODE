class Solution:
    def numTeams(self, rating):
        n = len(rating)
        res = 0
        
        for j in range(n):
            left_less = left_greater = 0
            right_less = right_greater = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                else:
                    left_greater += 1
            
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                else:
                    right_less += 1
            
            res += left_less * right_greater + left_greater * right_less
        
        return res