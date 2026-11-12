class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruthe force 
        profit=0
        buy=101
        for num in prices:
            buy=min(buy, num)
            profit=max(num-buy, profit)
        return profit

            
                


        