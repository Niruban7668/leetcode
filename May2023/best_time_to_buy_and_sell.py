class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/957274953/
#easy