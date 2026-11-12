class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=r=0
        Length=0
        while(r<len(nums)):
            while(r<len(nums) and nums[r]==1):
                r+=1
            Length=max(Length, r-l)
            l=r+1
            r+=1
        return Length

