class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # slidinfg window
        def helper(x:int)->int:
            # count subarrays at max x
            l, ct, Sum=0 ,0, 0
            for i in range(len(nums)):
                Sum+=nums[i]
                while(l<i and Sum>x):
                    Sum-=nums[l]
                    l+=1
                if Sum<=x:
                    ct+=(i-l)+1
            return ct
        return helper(goal)-helper(goal-1)       
        