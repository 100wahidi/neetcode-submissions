class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s = 0
        prod = 1
        l = 0
        for r in range(len(nums)):
            prod*=nums[r]
            while l<=r and prod >= k:
                prod = prod //nums[l]
                l+=1
            s +=(r-l+1)
        return s


                


        