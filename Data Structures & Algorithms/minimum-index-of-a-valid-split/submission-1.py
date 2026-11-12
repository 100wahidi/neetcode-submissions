class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # bruthe force 
        # who is the dominant
        dom, ct=0, 0
        for num in nums:
            if ct==0:
                dom=num
            if num==dom:
                ct+=1
            else:
                ct-=1
        Freq=0
        for e in nums:
            if dom==e:
                Freq+=1
        h=0
        ct=Freq
        for i in range(len(nums)):
            if nums[i]==dom:
                h+=1
            if h*2>i+1 and (ct-h)*2>(len(nums)-i-1):
                return i
        return -1
        