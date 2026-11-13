class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ct=0
        diff=0
        nums=sorted(nums)
        diff=float("infinity")
        r, l=0, 0
        for i in range(k-1, len(nums)):
            diff=min(diff, nums[i]-nums[i-k+1])


       
        return 0 if diff==float("infinity") else diff



        