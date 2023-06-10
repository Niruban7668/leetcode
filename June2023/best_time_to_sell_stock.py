class Solution:
    def maxProfit(self, prices):
        min1=prices[0]
        max1=0
        if(len(prices)==0 or len(prices)==1):
            return 0
        for i in range(0,(len(prices))):
            if(prices[i]<min1):
                min1=prices[i]
            max1=max(max1,prices[i]-min1)
        return max

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/968047326/
#easy