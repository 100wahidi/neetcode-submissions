class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ct=0
        L=0
        res=0
        Prd=1
        for r in range(len(nums)):
            Prd*=nums[r]
            while(L<=r and Prd>=k):
                Prd//=nums[L]
                L+=1
            res+=r-L+1
                
        return res
    



        