class Solution:
    def maxProfit(self, prices, fee):
        hold = -prices[0]
        cash = 0
        
        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)
        
        return cash