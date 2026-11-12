class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # bruthe force 
        # who is the dominant
        H_map={}
        for n in nums:
            H_map[n]=1+ H_map.get(n, 0)
        dom, ct=0, 0
        for e, f in H_map.items():
            if f>=ct:
                dom=e
                ct=f
        h=0
        for i in range(len(nums)):
            if nums[i]==dom:
                h+=1
            if h*2>i+1 and (ct-h)*2>(len(nums)-i-1):
                return i
            print(i, h, ct)
        return -1
        