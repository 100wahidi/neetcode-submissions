class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H_set={}
        for i, num in enumerate(nums):
            Diff=target-num
            if num in H_set:
                return [H_set[num], i]
            H_set[target-num]=i



        