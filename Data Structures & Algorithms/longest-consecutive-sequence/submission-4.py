class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        MaxLength=0
        for n in numsSet:
            curr = n
            length = 0
            if curr-1 not in numsSet:
                while curr in numsSet:
                    curr+=1
                    length+=1
                MaxLength = max(length, MaxLength)               

        return MaxLength


        