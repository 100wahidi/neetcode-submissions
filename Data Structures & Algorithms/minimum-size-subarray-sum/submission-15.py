class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Cs=0
        l=0
        Length=10000
        for ii in range(len(nums)):
            Cs+=nums[ii]
            while(l<=ii and Cs>=target):
                Length=min(Length, ii-l+1)
                Cs-=nums[l]
                l+=1
        if Length==10000:
            return 0
        return Length


        