class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimal solution 
        # binary search on rates 
        left, right= 1 , max(piles)
        while(left<right):
            midlle = (left+right)//2
            # if it is valid go left
            if self.utility(piles, midlle, h) is True:
                right= midlle
            else:
                left= midlle+1
        return left


    def utility(self,piles:list[int],  rate: int, h):
        hours=0
        count=0
        for pile in piles:
            count=pile//rate
            if count*rate==pile:
                hours+=count
            else:
                hours+=count+1
        if hours <= h:
            return True
        else:
            return False



            


        
        