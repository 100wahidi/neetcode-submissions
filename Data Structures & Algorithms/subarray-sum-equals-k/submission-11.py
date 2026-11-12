class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # use Helper 
        # key == sum, value: counting
        Hash_map={0:1}
        CumSum=0
        ct=0
        for i in range(len(nums)):
            CumSum+=nums[i]
            Diff=CumSum-k
            ct+=Hash_map.get(Diff, 0)
            Hash_map[CumSum]=1+ Hash_map.get(CumSum, 0)
        return ct
            
        
            




        