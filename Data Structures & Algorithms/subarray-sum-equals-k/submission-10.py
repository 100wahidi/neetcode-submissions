class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # optimal 
        ct=0
        CumSum=0
        H_map={0:1}
        for i,num in enumerate(nums):
            # cumulative sum
            CumSum+=num
            # the difference that recall the previous CumSums
            # if CumSum==Diff it means subarray == k 
            diff=CumSum-k
            ct+=H_map.get(diff, 0)
            H_map[CumSum]=1+H_map.get(CumSum, 0)
        return ct
        
        