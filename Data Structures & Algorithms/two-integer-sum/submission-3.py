class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        index = 0
        bindex = 0
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                sum = target - nums[i]
                index = i
            if nums[i]==sum:
               bindex = i
        return [index,bindex]

                
        