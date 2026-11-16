class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L=0
        count=0
        for R in range(len(nums)):
            L=R
            while(L<len(nums)-1 and nums[L]==val):
                L+=1
            nums[R], nums[L]=nums[L], nums[R]

        return len(nums)-nums.count(val)
            


        