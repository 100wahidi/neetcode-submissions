class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # slidinfg window
        def helper(x:int)->int:
            # count subarrays at max x
            if x<0:
                return 0
            l, ct, Sum=0 ,0, 0
            for i in range(len(nums)):
                Sum+=nums[i]
                while(l<i and Sum>x):
                    Sum-=nums[l]
                    l+=1
                if Sum<=x:
                    ct+=(i-l)+1
            return ct
        print(helper(goal),helper(goal-1))
        return helper(goal)-helper(goal-1)       
        