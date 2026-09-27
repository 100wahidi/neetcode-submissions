class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruthe force
        profit = 0
        buy= prices[0]
        h = {}
        for i in range(1,len(prices)):
            if buy < prices[i]:
                profit = max(profit, prices[i]-buy)
            if buy > prices[i]:
                buy = prices[i]

        return profit
                
            
