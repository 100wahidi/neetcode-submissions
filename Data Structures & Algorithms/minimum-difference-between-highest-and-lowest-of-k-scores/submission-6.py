class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        diff=float("infinity")
        for i in range(k-1, len(nums)):
            diff=min(diff, nums[i]-nums[i-k+1])

        return 0 if diff==float("infinity") else diff



        