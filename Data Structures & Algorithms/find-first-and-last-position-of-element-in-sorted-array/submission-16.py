class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums):
            l, r=0, len(nums)-1
            while(l<r):
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid
                    break
            if nums[r]!=target:
                return [-1, -1]
            c, d=1, 1
            while(r<=len(nums)-1-c and nums[r+c]==target):
                c+=1
            while(r>=d and nums[r-d]==target):
                d+=1

            return [r-d+1, r+c-1]
                    
        
        else:
            return [-1, -1]





        