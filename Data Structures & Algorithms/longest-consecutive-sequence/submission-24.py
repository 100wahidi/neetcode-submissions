class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        h=1
        maxiso=1
        Dists=set(sorted(nums))
        for num in Dists:
            if num-1 not in Dists:
                index=0
                h=0
                while(num+index in Dists):
                    index+=1
                    h+=1
                maxiso=max(maxiso, h)
            
        print(Dists)
        return maxiso

        