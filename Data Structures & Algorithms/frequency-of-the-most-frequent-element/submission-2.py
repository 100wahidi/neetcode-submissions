class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # manitain a window *
        Max=0
        ptr=1
        nums=sorted(nums)
        L, R=0, 0
        Sum=0
        for R in range(len(nums)):
            Sum+=nums[R]
            while((R-L+1)*nums[R]-Sum>k):
                Sum-=nums[L]
                L+=1
            Max=max((R-L+1), Max)
        return Max



        
        

        