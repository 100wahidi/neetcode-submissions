class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        H_set={}    
        for i in range(len(nums)):
            if i<=k:
                H_set[nums[i]]=H_set.get(nums[i], 0)+1
                if H_set[nums[i]]>=2:
                    return True
            else:
                H_set[nums[i]]=H_set.get(nums[i], 0)+1
                H_set[nums[i-k-1]]-=1
                if H_set[nums[i]]>=2:
                    return True
        return False

        