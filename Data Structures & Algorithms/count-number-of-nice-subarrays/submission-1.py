class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # count subarray
        H_map={0:1}
        ct=0
        NumSar=0
        for i, num in enumerate(nums):
            if num%2!=0:
                ct+=1
            diff=ct-k
            if diff in H_map:
                NumSar+=H_map[diff]
            H_map[ct]=1+H_map.get(ct, 0)
        return NumSar


