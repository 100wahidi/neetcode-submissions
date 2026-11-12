class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        else:
            # search from the first elemnt ofrotation 
            low, high= 0, len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                # search first that validate less than nums[-1]
                if nums[mid]>nums[-1]:
                    low=mid+1
                else:
                    high=mid-1
            return nums[low]
                