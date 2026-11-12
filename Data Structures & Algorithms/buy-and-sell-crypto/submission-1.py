class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        MaxP=0
        l, r=0, 1
        while(r<len(prices)):
            if prices[l]<prices[r]:
                MaxP=max(MaxP, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return MaxP



        
        