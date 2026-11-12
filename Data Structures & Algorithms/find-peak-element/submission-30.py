class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high=0, len(nums)-1
        while(low<high):
            middle=(low+high)//2
            if nums[middle]>nums[middle+1]:
                high=middle
            else:
                low=middle+1
        return low

        