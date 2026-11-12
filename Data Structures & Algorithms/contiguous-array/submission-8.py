class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # optimal 
        # i m going to represent 0 by -1
        # and return the longest with sum==0
        H_mp={}
        CumSum=0
        Length=0
        for i, num in enumerate(nums):
            if num==0:
               CumSum-=1
            else:
               CumSum+=1
            if CumSum not in H_mp:
                H_mp[CumSum]=i
            else:
                H_mp[CumSum]=min(i, H_mp.get(CumSum))
                Length=max(Length, i-H_mp[CumSum])
            if CumSum==0:
                Length=max(Length, i-min(H_mp[CumSum],0)+1)
        return Length


