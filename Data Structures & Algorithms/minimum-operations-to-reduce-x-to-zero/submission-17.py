class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        L=0
        res=0
        Cum=0
        print(x)
        if x<min(nums[0], nums[-1]):
            print(min(nums[0], nums[-1]))
            return -1
        for i in range(len(nums)):
            Cum+=nums[i]
            while(L<=i and Cum>target):
                Cum-=nums[L]
                L+=1
            if Cum==target:
                res=max(res, i-L+1)
        if sum(nums)!=x and res==0:
            return -1
        return len(nums)-res
            

 