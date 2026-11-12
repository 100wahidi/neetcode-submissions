class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=zeroes=0
        first=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
            while(zeroes>k):
                if nums[first]==0:
                    zeroes-=1
                # at the end went to the next First
                first+=1
            print(first)
            res=max(res, i-first+1)
        return res
            


