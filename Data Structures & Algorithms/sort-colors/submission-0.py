class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # search on nums
        # use bisecSearch for the min larsest than i value and exchange posiions:
        n = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, n):
                if nums[j]<=nums[i]:
                    nums[i], nums[j]=nums[j], nums[i]

        return nums


            
        