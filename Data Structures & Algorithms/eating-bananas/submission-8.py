class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(rate:int)->bool:
            i=0
            for pile in piles:
                eaten=pile
                if (eaten//rate)*rate==pile:
                    i+=eaten//rate
                else:
                    i+=eaten//rate +1
            return i<=h

  
        left, right=1, max(piles)
        while(left<=right):
            ptr = (left+right)//2
            if isValid(ptr):
                right=ptr-1
            else:
                left=ptr+1

        return left





        