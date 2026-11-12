class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxiso=1
        Dists=set(nums)
        for num in Dists:
            if num-1 not in Dists:
                index=0
                while(num+index in Dists):
                    index+=1
                maxiso=max(maxiso, index)
            
        print(Dists)
        return maxiso

        