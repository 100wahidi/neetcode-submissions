class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #bruthe force 
        ct=0
        for i in range(len(nums)):
            Curr=0
            for j in range(i, len(nums)):
                Curr+=nums[j]
                if Curr==goal:
                    ct+=1
        return ct

        