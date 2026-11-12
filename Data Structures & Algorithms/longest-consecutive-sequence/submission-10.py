class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums=sorted(nums)
            h=1
            maxisio=1
            print(nums)
            for i in range(1, len(nums)):
                if abs(nums[i]-nums[i-1])==1:
                    h+=1
                elif abs(nums[i]-nums[i-1])>1:
                    h=1
                else:
                    continue
                maxisio=max(h, maxisio)

            return maxisio
        else:
            return 0

        