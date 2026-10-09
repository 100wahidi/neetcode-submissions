class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        right = n-1
        left = 0
        while(left<right):
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            ptr = (left+right)//2
            if nums[ptr]==target:
                return ptr
            elif nums[ptr]>target:
                right=ptr-1
            elif nums[ptr]<target:
                left=ptr+1

            
        print(left,right)
        if target<=nums[right]:
            return left
        elif target>nums[right]:
            return right+1





            