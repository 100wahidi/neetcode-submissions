class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        h_map={}
        maxisio = 0
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            h_map[nums[i]]=h_map.get(nums[i], 0)+1
            if i>=k-1:
                if len(h_map)==k:
                    maxisio=max(maxisio, total)
                h_map[nums[i-k+1]]-=1
                if  h_map[nums[i-k+1]]==0:
                    h_map.pop(nums[i-k+1])
                total-=nums[i-k+1] 

        return maxisio
        

