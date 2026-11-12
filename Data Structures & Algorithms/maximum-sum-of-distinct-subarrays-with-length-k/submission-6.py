class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        h_map={}
        maxisio = 0
        total = 0
        ctr = 0
        for i in range(len(nums)):
            total+=nums[i]
            ctr+=1
            h_map[nums[i]]=h_map.get(nums[i], 0)+1
            if ctr==k:
                if len(h_map.keys())==k:
                    maxisio=max(maxisio, total)
                total-=nums[i-k+1] 
                h_map[nums[i-k+1]]-=1
                if  h_map[nums[i-k+1]]==0:
                    h_map.pop(nums[i-k+1])
                ctr-=1
        return maxisio
        

