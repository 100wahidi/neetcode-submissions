class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # optimal solution 
        Hash_map={0:1}
        prefix=0
        ct=0
        for i, num in enumerate(nums):
            prefix+=num
            diff=prefix-goal
            if diff>=0 and diff in Hash_map:
                ct+=Hash_map[diff]
            Hash_map[prefix]=1+Hash_map.get(prefix,0)
        return ct 

