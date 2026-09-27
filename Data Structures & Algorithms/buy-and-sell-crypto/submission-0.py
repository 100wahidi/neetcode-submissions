class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruthe force
        profit = 0
        for i in range(len(prices)):
            buy= prices[i]
            curr = 0
            for j in range(i+1,len(prices)):
                if buy < prices[j]:
                    curr = max(prices[j] - buy, curr)
            profit = max(profit, curr)

        return profit 
                
            
