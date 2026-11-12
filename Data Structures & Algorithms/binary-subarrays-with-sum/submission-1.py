class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # optimal solution 
        Hash_map={0:-1}
        prefix=0
        ct=0
        for i, num in enumerate(nums):
            prefix+=num
            diff=prefix-goal
            if diff>=0 and diff in Hash_map:
                ct+=1
                index=Hash_map[diff]+1
                while(index<i and nums[index]==0):
                    ct+=1
                    index+=1
            Hash_map[prefix]=Hash_map.get(prefix,i)
        return ct 

