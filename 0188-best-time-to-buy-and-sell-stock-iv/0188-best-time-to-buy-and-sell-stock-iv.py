class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0

        n = len(prices)

        # unlimited transactions case
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit

        buy = [float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = min(buy[i], price - sell[i-1])
                sell[i] = max(sell[i], price - buy[i])

        return sell[k]